import { ReactNode } from "react";
import UploadAreaText from "./UploadAreaText";

interface Props {
    children?: ReactNode;
}

const Header = ({ children }: Props) => {
    return (
        <header className="bg-slate-50 lg:fixed lg:inset-y-0 lg:left-0 lg:flex lg:w-100 lg:items-start lg:overflow-y-auto xl:w-100">
            <div className="relative z-10 mx-auto px-4 pb-4 pt-10 sm:px-6 md:max-w-sm md:px-4 lg:min-h-full lg:flex-auto lg:border-x lg:border-slate-200 flex items-center">
                <div className="flex items-center justify-content-center h-full flex-col">
                    {children}
                    <div className="mt-10 text-center lg:mt-12 lg:text-left px-6 mx-auto">
                        <UploadAreaText></UploadAreaText>
                    </div>
                </div>
            </div>
        </header>
    );
};

export default Header;
