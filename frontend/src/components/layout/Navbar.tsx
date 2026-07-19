"use client";

export default function Navbar() {
  return (
    <header className="bg-white border-b h-16 flex items-center justify-between px-8">
      <div>
        <h2 className="text-xl font-semibold">
          Dashboard
        </h2>
      </div>

      <div className="font-medium">
        IBM Project
      </div>
    </header>
  );
}