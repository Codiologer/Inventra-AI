"use client";

import { useEffect, useState } from "react";
import {
  Boxes,
  TriangleAlert,
  IndianRupee,
  ShoppingCart,
} from "lucide-react";

import { DashboardAPI } from "@/services/dashboard";
import { DashboardSummary } from "@/types/dashboard";

export default function SummaryCards() {

  const [summary, setSummary] =
    useState<DashboardSummary | null>(null);

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState("");

  useEffect(() => {

    async function fetchSummary() {

      try {

        const data = await DashboardAPI.summary();

        console.log("Dashboard Data =", data);

        setSummary(data);

        console.log(summary);

      }

      catch (err) {

        console.error("Dashboard Error:", err);

        setError("Failed to load dashboard");

        }

      finally {

        setLoading(false);

      }

    }

    fetchSummary();

  }, []);

  if (loading) {

    return (

      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

        {[1,2,3,4].map((item)=>(

          <div
            key={item}
            className="bg-white rounded-2xl h-40 animate-pulse"
          />

        ))}

      </div>

    );

  }

  if (error) {

    return (

      <div className="bg-red-100 text-red-700 rounded-xl p-5">

        {error}

      </div>

    );

  }

  const cards = [

    {

      title: "Total Products",

      value: summary?.total_products,

      icon: Boxes,

      color: "text-blue-600"

    },

    {

      title: "Revenue",

      value: `₹ ${summary?.total_revenue}`,

      icon: IndianRupee,

      color: "text-green-600"

    },

    {

      title: "Critical Stock",

      value: summary?.critical_products,

      icon: TriangleAlert,

      color: "text-red-600"

    },

    {

      title: "Quantity Sold",

      value: summary?.total_quantity_sold,

      icon: ShoppingCart,

      color: "text-orange-600"

    }

  ];

  return (

    <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">

      {cards.map((card) => (

        <div
          key={card.title}
          className="bg-white rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 p-6 border border-gray-100"
        >

          <div className="flex justify-between items-center">

            <div>

              <p className="text-gray-500">

                {card.title}

              </p>

              <h2 className="text-4xl font-bold mt-4">

                {card.value}

              </h2>

            </div>

            <card.icon
              size={40}
              className={card.color}
            />

          </div>

        </div>

      ))}

    </div>

  );

}