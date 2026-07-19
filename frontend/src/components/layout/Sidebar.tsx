"use client";

import {
  LayoutDashboard,
  Boxes,
  ShoppingCart,
  BarChart3,
  Bot,
  Settings,
} from "lucide-react";

const menu = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
  },
  {
    title: "Inventory",
    icon: Boxes,
  },
  {
    title: "Sales",
    icon: ShoppingCart,
  },
  {
    title: "Analytics",
    icon: BarChart3,
  },
  {
    title: "AI Assistant",
    icon: Bot,
  },
  {
    title: "Settings",
    icon: Settings,
  },
];

export default function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 text-white min-h-screen p-6">
      <h1 className="text-2xl font-bold mb-10">
        InventraAI
      </h1>

      <nav className="space-y-3">
        {menu.map((item) => (
          <button
            key={item.title}
            className="flex items-center gap-3 w-full px-4 py-3 rounded-xl hover:bg-slate-800 transition"
          >
            <item.icon size={20} />
            {item.title}
          </button>
        ))}
      </nav>
    </aside>
  );
}