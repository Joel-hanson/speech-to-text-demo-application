// UploadArea.tsx
import React, { useRef, useState } from "react";

interface UploadAreaProps {
    handleFileUpload: (file: File | undefined) => void;
    uploadedFile?: File;
}

const UploadArea: React.FC<UploadAreaProps> = ({
    handleFileUpload: handleFileUpload,
    uploadedFile: uploadedFile,
}) => {

    const [uploadReady, setUploadReady] = useState(false);
    const uploadAreaRef = useRef<HTMLDivElement>(null);

    const preventDefaults = (event: React.DragEvent) => {
        event.preventDefault();
        event.stopPropagation();
    };

    const highlight = (event: React.DragEvent) => {
        preventDefaults(event);
        uploadAreaRef.current?.classList.add("bg-blue-300");
    };

    const unhighlight = (event: React.DragEvent) => {
        preventDefaults(event);
        uploadAreaRef.current?.classList.remove("bg-blue-300");
    };

    const handleDrop = (event: React.DragEvent) => {
        unhighlight(event);
        const file = event.dataTransfer?.files[0];

        if (file) {
            handleFileUpload(file);
            setUploadReady(true);
        }
    };

    const handleFileInputChange = (event: React.ChangeEvent<HTMLInputElement>): void => {
        const file = event.target.files?.[0];
        if (file) {
            handleFileUpload(file);
            setUploadReady(true);
        }
    };
    return (
        <div
            className="relative z-10 mx-auto px-4 pb-4 pt-10 sm:px-6 md:max-w-sm md:px-4 lg:min-h-full lg:flex-auto flex items-center"
        >
            <div
                ref={uploadAreaRef}
                className="relative mx-auto w-80 overflow-hidden shadow-xl shadow-slate-200 sm:w-96 sm:rounded-xl lg:rounded-2xl flex items-center justify-center font-sans rounded-xl border-2 border-dashed border-blue-400 bg-white lg:w-full xl:min-h-[25vh] lg:min-h-[25vh] sm:min-h-min md:min-h-min"
                id="drop-area"
                onDragEnter={highlight}
                onDragOver={highlight}
                onDragLeave={unhighlight}
                onDrop={handleDrop}
            >
                <label
                    htmlFor="dropzone-file"
                    className="mx-auto cursor-pointer flex flex-col items-center p-5 text-center"
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
                        onChange={handleFileInputChange}
                    />
                    <>{uploadFileInfo(uploadedFile)}</>
                    <button
                        id="upload-button"
                        className="w-full inline-flex items-center justify-center px-4 py-2 my-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                        style={{ display: uploadReady ? "block" : "none" }}
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

function uploadFileInfo(file: File | undefined) {
    if (file) {
        console.log("file: ", file);
        return (
            <div className="mx-auto p-2 my-2 mt-4 text-left text-sm font-mono text-gray-500 bg-gray-100">
                <h2 className="mt-4 text-xl font-medium text-slate-700">
                    {file.name}
                </h2>
                <p className="font-mono text-sm order-first leading-7 text-slate-500 float-left inline p-1">
                    {bytesToSize(file.size)}
                </p>
                <p className="text-xs leading-7 text-slate-700 float-right inline p-1">
                    Type: {(file.type || "n/a").toUpperCase()}
                </p>
            </div>
        );
    }
}

function bytesToSize(bytes: number) {
    const sizes = ["Bytes", "KB", "MB", "GB", "TB"];
    if (bytes == 0) return "n/a";
    if (!bytes) return "n/a";
    const i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)).toString());
    if (i == 0) return bytes + " " + sizes[i];
    return (bytes / Math.pow(1024, i)).toFixed(1) + " " + sizes[i];
}

export default UploadArea;
