export interface DashboardSummary {
  total_products: number;
  low_stock_products: number;
  critical_products: number;
  total_inventory: number;
  total_revenue: number;
  total_quantity_sold: number;
}

export interface AlertItem {
  type: string;
  product: string;
  message: string;
}

export interface TopProduct {
  product: string;
  quantity_sold: number;
  revenue: number;
}

export interface SalesAnalytics {
  date: string;
  sales: number;
  revenue: number;
}