import { useEffect } from "react";
import AnimatedText from "./AnimatedText";
import ItemStatus, { getStepIndex } from "./ItemStatus";
import ListenButton from "./ListenButton";
import TextContentLoader from "./TextContentLoader";

export type Upload = {
    id: number;
    file: string;
    created_at: string;
    updated_at: string;
};

export type UploadItemProps = {
    id: number;
    file: string;
    created_at: string;
    updated_at: string;
    uploads: Upload[];
};

export type UploadDetailsProps = {
    id: number;
    text: string;
    service: string;
    status: string;
    date: string;
    time: string;
    title: string;
    upload: Upload;
};


const UploadItem = ({ item }: { item: UploadDetailsProps }) => {
    useEffect(() => {
        console.log(`UploadItem: ${item.id} - ${item.title} - ${item.status}`);
    }, [item]);

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
                                {item.title}
                            </h2>
                            <time
                                className="order-first font-mono text-sm leading-7 text-slate-500"
                            >
                                {item.date}
                            </time>
                            <time
                                className="order-first font-mono text-xs leading-7 text-slate-500"
                            >
                                {item.time}
                            </time>
                            {/* <TypedText text={item.text} delay={30} /> */}

                            {getStepIndex(item.status) <= 2 ? (
                                <TextContentLoader></TextContentLoader>
                            ) : (
                                getStepIndex(item.status) == 3 ?
                                    <AnimatedText text={item.text} /> : <AnimatedText text={"Failed to process the file"} />
                            )}
                            <ItemStatus status={item.status} />
                            <ListenButton link={item.upload.file} />
                        </div>
                    </div>
                </div>
            </div>
        </article>
    );
};

export default UploadItem;
