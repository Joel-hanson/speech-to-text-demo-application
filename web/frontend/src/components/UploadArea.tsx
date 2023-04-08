// UploadArea.tsx
import React, { useRef } from "react";

interface UploadAreaProps {
    handleFileUpload: (file: string) => void;
    uploadedFile?: string;
}

const UploadArea: React.FC<UploadAreaProps> = ({
    handleFileUpload: handleFileUpload,
    uploadedFile: uploadedFile,
}) => {
    const uploadAreaRef = useRef<HTMLDivElement>(null);

    const preventDefaults = (event: React.DragEvent) => {
        event.preventDefault();
        event.stopPropagation();
    };

    const highlight = (event: React.DragEvent) => {
        uploadAreaRef.current?.classList.add("highlight");
    };

    const unhighlight = (event: React.DragEvent) => {
        uploadAreaRef.current?.classList.remove("highlight");
    };

    const handleDrop = (event: React.DragEvent) => {
        preventDefaults(event);
        unhighlight(event);

        const file = event.dataTransfer?.files[0];

        if (file) {
            const reader = new FileReader();
            reader.onload = () => {
                const result = reader.result as string;
                handleFileUpload(result);
            };
            reader.readAsDataURL(file);
        }
    };

    return (
        <div
            ref={uploadAreaRef}
            className="relative z-10 mx-auto px-4 pb-4 pt-10 sm:px-6 md:max-w-sm md:px-4 lg:min-h-full lg:flex-auto flex items-center"
            id="drop-area"
            onDragEnter={highlight}
            onDragOver={highlight}
            onDragLeave={unhighlight}
            onDrop={handleDrop}
        >
            <div
                className="relative mx-auto w-80 overflow-hidden shadow-xl shadow-slate-200 sm:w-96 sm:rounded-xl lg:rounded-2xl flex items-center justify-center font-sans rounded-xl border-2 border-dashed border-blue-400 bg-white lg:w-full xl:min-h-[25vh] lg:min-h-[25vh] sm:min-h-min md:min-h-min"
                id="drop-area"
            >
                <label
                    htmlFor="dropzone-file"
                    className="mx-auto cursor-pointer flex flex-col items-center p-6 text-center"
                >
                    {uploadIcon()}
                    <h2 className="mt-4 text-xl font-medium text-gray-700 tracking-wide upload-label-information">
                        Audio File
                    </h2>
                    <p className="mt-2 text-gray-500 tracking-wide upload-label-information">
                        Upload or drag &amp; drop a WAV file.{" "}
                    </p>
                    <input
                        id="dropzone-file"
                        type="file"
                        className="hidden upload-label-information"
                    />
                    <div
                        id="upload-file-details"
                        className="mx-auto px-4 flex flex-col text-left"
                    >{uploadFileInfo(uploadedFile)}</div>
                    <button
                        id="upload-button"
                        className="mt-24 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded text-right"
                        style={{ display: "none" }}
                    >
                        Upload
                    </button>
                </label>
            </div>
        </div>
    );
};

function uploadIcon() {
    return (
        <svg
            xmlns="http://www.w3.org/2000/svg"
            className="h-10 w-10 text-blue-500 upload-label-information"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            strokeWidth="2"
        >
            <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
            />
        </svg>
    );
}

function uploadFileInfo(file: string) {
    if (file) {
        return (
            <div>
                <h2 className="mt-4 text-xl font-medium text-slate-700">
                    {/* {file.name} */}
                </h2>
                <p className="font-mono text-sm order-first leading-7 text-slate-500">
                    {/* {file.size} bytes */}
                </p>
                <p className="mt-1 text-xs leading-7 text-slate-700">
                    {/* Type: {(file.type || "n/a").toUpperCase()} */}
                </p>
            </div>
        );
    }
}

export default UploadArea;
