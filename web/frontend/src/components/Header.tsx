import { ReactNode } from "react";
import UploadAreaText from "./UploadAreaText";

interface Props {
    children?: ReactNode;
}

const Header = ({ children }: Props) => {
    return (
        <header className="bg-slate-50 lg:fixed lg:inset-y-0 lg:left-0 lg:flex lg:w-96 lg:items-start lg:overflow-y-auto xl:w-96">
            <div className="relative z-10 mx-auto px-4 pb-4 pt-10 sm:px-6 md:max-w-sm md:px-4 lg:min-h-full lg:flex-auto lg:border-x lg:border-slate-200">
                <div className="flex items-center justify-content-center h-full flex-col">
                    <div className="text-center lg:text-left px-6 mx-auto">
                        <UploadAreaText></UploadAreaText>
                    </div>
                    {children}
                </div>
            </div>
        </header>
    );
};

export default Header;
