import api from "@/services/api";
import { Product } from "@/types/inventory";

export const InventoryAPI = {
  async getProducts(): Promise<Product[]> {
    const res = await api.get("/api/v1/products");
    return res.data;
  },

  async getProduct(id: number): Promise<Product> {
    const res = await api.get(`/api/v1/products/${id}`);
    return res.data;
  },

  async createProduct(data: Partial<Product>) {
    return api.post("/api/v1/products", data);
  },

  async updateProduct(id: number, data: Partial<Product>) {
    return api.put(`/api/v1/products/${id}`, data);
  },

  async deleteProduct(id: number) {
    return api.delete(`/api/v1/products/${id}`);
  },
};