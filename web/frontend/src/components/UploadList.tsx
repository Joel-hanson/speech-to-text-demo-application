import { useEffect, useState } from 'react';

import useWebSocket, { ReadyState } from 'react-use-websocket';
import { S2T_WS_URL, getDetailedListOfUploads } from '../helpers/ApiUtils';
import UploadItem, { UploadDetailsProps } from './UploadItem';
// import svg from assets

type SocketMessageData = {
    "type": string,
    "data": UploadDetailsProps
}

type SocketDataType = {
    "message": SocketMessageData
}
type SocketMessage = {
    data: SocketDataType
};


const UploadList = () => {
    //Public API that will echo messages sent to it back to the client
    const [socketUrl, setSocketUrl] = useState(S2T_WS_URL + 'lobby/');
    const [messageHistory, setMessageHistory] = useState<SocketMessage[]>([]);
    const [uploadedItems, setUploadedItems] = useState<UploadDetailsProps[]>([]);

    const { sendMessage, lastMessage, readyState } = useWebSocket(socketUrl, {
        shouldReconnect: (closeEvent) => true
    });

    useEffect(() => {
        if (lastMessage !== null) {
            setMessageHistory((prev) => prev.concat(lastMessage));
            let socket_data: SocketDataType = JSON.parse(lastMessage.data)
            let message: SocketMessageData = socket_data.message;
            console.log(message);

            let message_type = message.type;
            let data = message.data;
            let id = data.id;

            if (message_type === 'status_update') {
                // update object if already present or update the list
                setUploadedItems((prev) => {
                    let index = prev.findIndex((item) => item.id === id);
                    if (index !== -1) {
                        prev[index] = data;
                        return prev;
                    }
                    // append to the first of the list
                    return [data, ...prev];
                });
            }
        }
    }, [lastMessage, setMessageHistory]);


    // const handleClickSendMessage = useCallback(() => sendMessage(
    //     JSON.stringify({
    //         'type': 'frontend.message',
    //         'message': 'Hello World',
    //     })
    // ), []);

    const connectionStatus = {
        [ReadyState.CONNECTING]: 'Connecting',
        [ReadyState.OPEN]: 'Open',
        [ReadyState.CLOSING]: 'Closing',
        [ReadyState.CLOSED]: 'Closed',
        [ReadyState.UNINSTANTIATED]: 'Uninstantiated',
    }[readyState];

    useEffect(() => {
        getDetailedListOfUploads().then((data: UploadDetailsProps[] | any) => {
            setUploadedItems(data);
        });
    }, []);


    return (
        <main className="border-t border-slate-200 lg:relative lg:mb-28 lg:ml-96 lg:border-t-0 xl:ml-96">
            {showWebsocketStatus(connectionStatus)}
            <div className="relative">
                {/* <span>The WebSocket is currently {connectionStatus}</span>
                        {lastMessage ? <span>Last message: {lastMessage.data}</span> : null}
                        <ul>
                            {messageHistory.map((message, idx) => (
                                <span key={idx}>{message ? message?.data : null}</span>
                            ))}
                        </ul>
                        <button onClick={handleClickSendMessage}>Send Message</button> */}
                {/* show websocket in a beautiful way using indicators */}
                <div className="pb-12 pt-16 sm:pb-4 lg:pt-12">
                    <div className="lg:px-8">
                        <div className="lg:max-w-4xl">
                            <div className="mx-auto px-4 sm:px-6 md:max-w-2xl md:px-4 lg:px-0">
                                <h1 className="text-2xl font-bold leading-7 text-slate-700">
                                    Uploads
                                </h1>
                            </div>
                        </div>
                    </div>
                    <div className="divide-y divide-slate-100 sm:mt-4 lg:mt-8 lg:border-t lg:border-slate-100">
                        {messageHistory.length === 0 && uploadedItems.length === 0 ? (
                            <div className="flex flex-col items-center justify-center h-96">
                                <div className="flex flex-col items-center justify-center">
                                    <svg className="h-12 w-12 text-slate-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                                    </svg>
                                    {/* <img src={"static/audio_conversation.svg"} alt="audio conversation" /> */}

                                    <p className="mt-2 text-sm font-medium text-slate-500">No uploads yet</p>
                                </div>
                            </div>
                        ) : null
                        }
                        {/* {messageHistory.map((message, idx) => {
                            console.log('message', message);
                            return <UploadItem key={idx} item={message?.data ? JSON.parse(message.data) : {}} />
                        })} */}
                        {uploadedItems.map((item: UploadDetailsProps) => (
                            <UploadItem key={item.id} item={item} />
                        ))}
                    </div>
                </div>
            </div>
        </main>
    );
};

function showWebsocketStatus(connectionStatus: string) {
    return <div className="inset-0 flex p-2.5">
        <div className="flex-1 flex items-center justify-end">
            <div className="flex items-center space-x-3">
                {/* <div className="flex-1 min-w-0">
                    <p className="text-sm font-semibold text-gray-900 truncate">
                        WebSocket
                    </p>
                </div> */}
                {connectionStatus === 'Open' ? (
                    <>
                        {/* <span className="inline-flex items-center bg-green-100 text-green-800 text-xs font-medium rounded-full"> */}
                        <span className="w-1 h-1 mr-1 bg-green-500 rounded-full animate-ping"></span>
                        {/* Open */}
                        {/* </span> */}
                    </>
                ) : (
                    <>
                        {/* <span className="inline-flex items-center bg-red-100 text-red-800 text-xs font-medium rounded-full p-2"> */}
                        <span className="w-1 h-1 mr-1 ml-1 bg-red-500 rounded-full animate-pulse"></span>
                        {/* </span> */}
                    </>
                )}
            </div>
        </div>
    </div >;
}

export default UploadList;
