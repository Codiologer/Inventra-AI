import api from "./api";

export const DashboardAPI = {
  summary: async () => {
    const res = await api.get("/dashboard/summary");
    return res.data;
  },

  alerts: async () => {
    const res = await api.get("/dashboard/alerts");
    return res.data;
  },

  topProducts: async () => {
    const res = await api.get("/dashboard/top-products");
    return res.data;
  },

  salesAnalytics: async () => {
    const res = await api.get("/dashboard/sales-analytics");
    return res.data;
  },
};