from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd

@api_view(['GET'])
def portfolio_holdings(request):
    df = pd.read_excel('Sample Portfolio Dataset for Assignment.xlsx')
    holdings = []
    for _, row in df.iterrows():
        value = row['Quantity'] * row['Current Price (₹)']
        gain = value - (row['Quantity'] * row['Avg Price ₹'])
        gain_percent = (gain / (row['Quantity'] * row['Avg Price ₹'])) * 100
        holdings.append({
            'symbol': row['Symbol'],
            'name': row['Company Name'],
            'quantity': row['Quantity'],
            'avgPrice': row['Avg Price ₹'],
            'currentPrice': row['Current Price (₹)'],
            'sector': row['Sector'],
            'marketCap': row['Market Cap'],
            'value': round(value, 2),
            'gainLoss': round(gain, 2),
            'gainLossPercent': round(gain_percent, 2),
        })
    return Response(holdings)

@api_view(['GET'])
def portfolio_allocation(request):
    df = pd.read_excel('Sample Portfolio Dataset for Assignment.xlsx')
    by_sector = df.groupby('Sector')['Current Price (₹)'].sum().to_dict()
    by_market_cap = df.groupby('Market Cap')['Current Price (₹)'].sum().to_dict()
    
    total_sector = sum(by_sector.values())
    total_cap = sum(by_market_cap.values())

    response = {
        'bySector': {
            sector: {
                'value': round(value, 2),
                'percentage': round((value / total_sector) * 100, 1)
            } for sector, value in by_sector.items()
        },
        'byMarketCap': {
            cap: {
                'value': round(value, 2),
                'percentage': round((value / total_cap) * 100, 1)
            } for cap, value in by_market_cap.items()
        }
    }
    return Response(response)

@api_view(['GET'])
def portfolio_performance(request):
    data = {
        "timeline": [
            {"date": "2024-01-01", "portfolio": 650000, "nifty50": 21000, "gold": 62000},
            {"date": "2024-03-01", "portfolio": 680000, "nifty50": 22100, "gold": 64500},
            {"date": "2024-06-01", "portfolio": 700000, "nifty50": 23500, "gold": 68000}
        ],
        "returns": {
            "portfolio": {"1month": 2.3, "3months": 8.1, "1year": 15.7},
            "nifty50": {"1month": 1.8, "3months": 6.2, "1year": 12.4},
            "gold": {"1month": -0.5, "3months": 4.1, "1year": 8.9}
        }
    }
    return Response(data)

@api_view(['GET'])
def portfolio_summary(request):
    df = pd.read_excel('Sample Portfolio Dataset for Assignment.xlsx')
    df['Value'] = df['Quantity'] * df['Current Price (₹)']
    df['Gain'] = df['Value'] - (df['Quantity'] * df['Avg Price ₹'])
    df['GainPercent'] = (df['Gain'] / (df['Quantity'] * df['Avg Price ₹'])) * 100

    total_value = df['Value'].sum()
    total_invested = (df['Quantity'] * df['Avg Price ₹']).sum()
    total_gain = df['Gain'].sum()

    top = df.loc[df['GainPercent'].idxmax()]
    worst = df.loc[df['GainPercent'].idxmin()]

    response = {
        'totalValue': round(total_value, 2),
        'totalInvested': round(total_invested, 2),
        'totalGainLoss': round(total_gain, 2),
        'totalGainLossPercent': round((total_gain / total_invested) * 100, 2),
        'topPerformer': {
            'symbol': top['Symbol'],
            'name': top['Company Name'],
            'gainPercent': round(top['GainPercent'], 2)
        },
        'worstPerformer': {
            'symbol': worst['Symbol'],
            'name': worst['Company Name'],
            'gainPercent': round(worst['GainPercent'], 2)
        },
        'diversificationScore': 8.2,
        'riskLevel': 'Moderate'
    }
    return Response(response)