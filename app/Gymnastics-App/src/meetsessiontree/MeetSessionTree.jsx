import { useState } from "react";
import { ChevronUpIcon, ChevronDownIcon, PhotoIcon, FolderIcon, DocumentIcon } from "@heroicons/react/24/outline"


function TreeNode({ node, level = 0, onSelect, selectedName }) {
    const [open, setOpen] = useState(true);
    const hasChildren = node.children?.length > 0;
    const isSelected = selectedName === node.name;

    const Icon =
        node.type === "folder" ? FolderIcon : node.type === "image" ? PhotoIcon : DocumentIcon;

    return (
        <div>
            <div
                className={`flex items-center gap-2 py-1.5 px-2 rounded cursor-pointer ${isSelected ? "bg-indigo-500 text-white" : "text-black hover:bg-gray-100"
                    }`}
                style={{ paddingLeft: `${level * 1.5 + 0.5}rem` }}
                onClick={() => {
                    if (hasChildren) {
                        setOpen(!open);
                    } else {
                        onSelect?.(node);
                    }
                }}
            >
                <Icon className="w-4 h-4 shrink-0" />
                <span>{node.name}</span>
                {hasChildren && (
                    <span className="ml-auto pr-2">
                        {open ? <ChevronUpIcon className="w-4 h-4" /> : <ChevronDownIcon className="w-4 h-4" />}
                    </span>
                )}
            </div>

            {hasChildren && open && (
                <div
                    className="border-l border-gray-300"
                    style={{ marginLeft: `${level * 1.5 + 1.25}rem` }}
                >
                    {node.children.map((child, i) => (
                        <TreeNode
                            key={i}
                            node={child}
                            level={level + 1}
                            onSelect={onSelect}
                            selectedName={selectedName}
                        />
                    ))}
                </div>
            )}
        </div>
    );
}

function MeetSessionTree({ data, onSelect, selectedName }) {
    return (
        <div className="card bg-white shadow-sm w-full">
            <div className="card-body">
                <div className="bg-white rounded-2xl p-4 h-80 overflow-y-auto">
                    {data.map((node, i) => (
                        <TreeNode
                            key={i}
                            node={node}
                            onSelect={onSelect}
                            selectedName={selectedName}
                        />
                    ))}
                </div>
            </div>
        </div>
    );
}

export default MeetSessionTree;