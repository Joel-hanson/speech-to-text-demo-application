import ListenButton from "./ListenButton";

const UploadItem = () => {
    return (
        <article aria-labelledby="episode-5-title" className="py-10 sm:py-12">
            <div className="lg:px-8">
                <div className="lg:max-w-4xl">
                    <div className="mx-auto px-4 sm:px-6 md:max-w-2xl md:px-4 lg:px-0">
                        <div className="flex flex-col items-start">
                            <h2
                                id="episode-5-title"
                                className="mt-2 text-lg font-bold text-slate-900"
                            >
                                Bill Lumbergh
                            </h2>
                            <time
                                dateTime="2022-02-24T00:00:00.000Z"
                                className="order-first font-mono text-sm leading-7 text-slate-500"
                            >
                                February 24, 2022
                            </time>
                            <p className="mt-1 text-base leading-7 text-slate-700">
                                He’s going to need you to go ahead and come in on Saturday, but
                                there’s a lot more to the story than you think.
                            </p>
                            {stepper()}
                            <ListenButton />
                        </div>
                    </div>
                </div>
            </div>
        </article>
    );
};

function stepper() {
    return (
        <ol className="flex items-center w-full text-sm font-medium text-center text-gray-500 dark:text-gray-400 mt-4 gap-4 bg-gray-100 p-4 rounded-md">
            <li className="flex md:w-full items-center text-blue-600 dark:text-blue-500 sm:after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700">
                <span className="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500">
                    <svg
                        aria-hidden="true"
                        className="w-4 h-4 mr-2 sm:w-4 sm:h-4"
                        fill="currentColor"
                        viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path
                            fill-rule="evenodd"
                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                            clip-rule="evenodd"
                        ></path>
                    </svg>
                    Personal <span className="hidden sm:inline-flex sm:ml-2">Info</span>
                </span>
            </li>
            <li className="flex md:w-full items-center after:content-[''] after:w-full after:h-1 after:border-b after:border-gray-200 after:border-1 after:hidden sm:after:inline-block after:mx-6 xl:after:mx-10 dark:after:border-gray-700">
                <span className="flex items-center after:content-['/'] sm:after:hidden after:mx-2 after:text-gray-200 dark:after:text-gray-500">
                    <span className="mr-2">2</span>
                    Account <span className="hidden sm:inline-flex sm:ml-2">Info</span>
                </span>
            </li>
            <li className="flex items-center">
                <span className="mr-2">3</span>
                Confirmation
            </li>
        </ol>
    );
}

export default UploadItem;
