export interface Product {
  id: number;

  name: string;

  sku: string;

  category: string;

  stock_quantity: number;

  minimum_stock: number;

  supplier: string;

  lead_time_days: number;

  unit_price: number;

  created_at?: string;

  updated_at?: string;
}