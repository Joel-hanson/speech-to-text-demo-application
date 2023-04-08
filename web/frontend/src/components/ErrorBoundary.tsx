import { Component, ErrorInfo, ReactNode } from "react";

interface Props {
    children?: ReactNode;
}

interface State {
    hasError: boolean;
}

class ErrorBoundary extends Component<Props, State> {
    public state: State = {
        hasError: false
    };

    public static getDerivedStateFromError(_: Error): State {
        // Update state so the next render will show the fallback UI.
        return { hasError: true };
    }

    public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
        console.error("Uncaught error:", error, errorInfo);
    }

    public render() {
        if (this.state.hasError) {
            return (
                <div className="flex flex-col items-center justify-center h-screen">
                    <h1 className="text-4xl font-bold text-slate-900">
                        Something went wrong
                    </h1>
                    <p className="mt-3 text-lg font-light leading-8 text-slate-600">
                        Please refresh the page and try again.
                    </p>
                </div>
            )
        }

        return this.props.children;
    }
}

export default ErrorBoundary;