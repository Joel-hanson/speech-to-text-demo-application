import React from "react";

const ItemStatus: React.FC<{ status: string }> = ({ status }) => {
    let status_index = getStepIndex(status)
    const stepAnimation = status_index !== 3 && status_index !== 4
        ? " animate-pulse"
        : "";
    return (
        <ol className="flex items-center w-full text-sm font-medium text-center text-gray-500 dark:text-gray-400 mt-4 gap-4 bg-gray-100 p-4 rounded-md">
            {/* <li className="flex md:w-full items-center text-teal-600 dark:text-teal-500 sm:after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700"> */}
            <li
                className={
                    `flex md:w-full items-center after:w-full after:h-1 after:border-b after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 after:border-gray-700 ` +
                    (status_index >= 1
                        ? "text-teal-600 dark:text-teal-500 sm:after:content-['']"
                        : "after:content-['']") +
                    stepAnimation
                }
            >
                <span className="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500">
                    {status_index >= 1 ? (
                        tickSvg()
                    ) : (
                        <span className="mr-2">1</span>
                    )}
                    Processing{" "}
                    <span className="hidden sm:inline-flex sm:ml-2">Started</span>
                </span>
            </li>
            <li
                className={
                    `flex md:w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 after:border-gray-700 ` +
                    (status_index >= 2
                        ? "text-teal-600 dark:text-teal-500 sm:after:content-['']"
                        : "after:content-['']") +
                    stepAnimation
                }
            >
                <span className="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500">
                    {status_index >= 2 ? (
                        tickSvg()
                    ) : (
                        <span className="mr-2">2</span>
                    )}
                    Recogniting{" "}
                    <span className="hidden sm:inline-flex sm:ml-2">Text</span>
                </span>
            </li>
            <li
                className={
                    `flex items-center` +
                    (status_index >= 3 ? "text-teal-600 dark:text-teal-500" : "")
                }
            >
                {status_index >= 3 ? (
                    tickSvg()
                ) : (
                    <span className="mr-2">3</span>
                )}
                Completed
            </li>
        </ol>
    );
};

const StepperStatus = {
    Started: 1,
    Processing: 2,
    Completed: 3,
    Failed: 4,
};

function getStepIndex(status: string) {
    switch (status) {
        case "STARTED":
            return StepperStatus.Started;
        case "PROCESSING":
            return StepperStatus.Processing;
        case "COMPLETED":
            return StepperStatus.Completed;
        case "FAILED":
            return StepperStatus.Failed;
        default:
            return StepperStatus.Started;
    }
}

function tickSvg() {
    return (
        <svg
            aria-hidden="true"
            className="w-4 h-4 mr-2 sm:w-4 sm:h-4"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
        >
            <path
                fillRule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clipRule="evenodd"
            ></path>
        </svg>
    );
}

export default ItemStatus;
