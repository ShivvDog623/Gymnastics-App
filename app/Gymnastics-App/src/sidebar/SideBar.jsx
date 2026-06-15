import NavBar from "../navbar/Navbar"
import Home from "../pages/Home"
import Admin from "../pages/Admin"
import CreateMeetPage from "../pages/CreateMeetPage"
import { Routes, Route } from "react-router-dom"

import { HomeIcon, Cog6ToothIcon, ChartBarIcon, UsersIcon, KeyIcon, ComputerDesktopIcon, FolderOpenIcon } from "@heroicons/react/24/outline"

const navItems = [
    { label: "Homepage", icon: HomeIcon },
    { label: "Admin", icon: KeyIcon },
    { label: "Gymnasts", icon: UsersIcon },
    { label: "Display", icon: ComputerDesktopIcon },
    { label: "All Meets", icon: FolderOpenIcon },
    { label: "Settings", icon: Cog6ToothIcon },
]

function SideBar() {
    return (
        <div className="drawer lg:drawer-open">
            <input id="my-drawer-4" type="checkbox" className="drawer-toggle" />
            <div className="drawer-content">
                <NavBar />
                <div className="p-4">
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/admin" element={<Admin />} />
                        <Route path="/create-meet" element={<CreateMeetPage />} />
                    </Routes>
                </div>
            </div>

            <div className="drawer-side is-drawer-close:overflow-visible">
                <label htmlFor="my-drawer-4" aria-label="close sidebar" className="drawer-overlay"></label>
                <div className="flex min-h-full flex-col items-start bg-base-200 is-drawer-close:w-14 is-drawer-open:w-64">
                    <ul className="menu w-full grow p-0">
                        {navItems.map((item) => (
                            <li key={item.label}>
                                <button className="is-drawer-close:tooltip is-drawer-close:tooltip-right border-b mb-1" data-tip={item.label}>
                                    <item.icon className="size-6 shrink-0 flex justify-center ml-1" />
                                    <span className="is-drawer-close:hidden text-xl ml-1">{item.label}</span>
                                </button>
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default SideBar;