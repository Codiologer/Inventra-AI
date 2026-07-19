import "./globals.css";
import Providers from "@/providers/QueryProviders";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "InventraAI",
  description: "AI Powered Inventory Management",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {

  return (
    <html lang="en">

      <body>

        <Providers>

          {children}

        </Providers>
        
      </body>

    </html>
  );
}