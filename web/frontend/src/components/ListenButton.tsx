const ListenButton = ({ link }: { link: string }) => {
    return (
        <div className="mt-4 flex items-center gap-4">
            <button
                type="button"
                className="flex items-center text-sm font-bold leading-6 text-teal-500 hover:text-teal-700 active:text-teal-900"
                onClick={() => {
                    window.open(
                        link,
                        "_blank"
                    );
                }}
            >
                <svg
                    aria-hidden="true"
                    viewBox="0 0 10 10"
                    fill="none"
                    className="h-2.5 w-2.5 fill-current"
                >
                    <path d="M8.25 4.567a.5.5 0 0 1 0 .866l-7.5 4.33A.5.5 0 0 1 0 9.33V.67A.5.5 0 0 1 .75.237l7.5 4.33Z"></path>
                </svg>
                <span className="ml-3" aria-hidden="true">
                    Listen
                </span>
            </button>
        </div>
    );
};

export default ListenButton;
