import AppLayout from "@/components/layout/AppLayout";
import SummaryCards from "@/components/dashboard/SummaryCards";

export default function HomePage() {

  return (

    <AppLayout>

      <div className="space-y-8">

        <div>

          <h1 className="text-4xl font-bold">

            InventraAI Dashboard

          </h1>

          <p className="text-slate-500 mt-2">

            AI Powered Inventory Management Platform

          </p>

        </div>

        <SummaryCards />

      </div>

    </AppLayout>

  );

}