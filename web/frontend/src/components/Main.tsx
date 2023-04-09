import UploadItem from "./UploadItem";

const Main = () => {
    return (
        <main className="border-t border-slate-200 lg:relative lg:mb-28 lg:ml-96 lg:border-t-0 xl:ml-96">
            <div className="relative">
                <div className="pb-12 pt-16 sm:pb-4 lg:pt-12">
                    <div className="lg:px-8">
                        <div className="lg:max-w-4xl">
                            <div className="mx-auto px-4 sm:px-6 md:max-w-2xl md:px-4 lg:px-0">
                                <h1 className="text-2xl font-bold leading-7 text-slate-900">
                                    Uploads
                                </h1>
                            </div>
                        </div>
                    </div>
                    <div className="divide-y divide-slate-100 sm:mt-4 lg:mt-8 lg:border-t lg:border-slate-100">
                        <UploadItem />
                        <UploadItem />
                        <UploadItem />
                        <UploadItem />
                        <UploadItem />
                    </div>
                </div>
            </div>
        </main>
    );
};

export default Main;
