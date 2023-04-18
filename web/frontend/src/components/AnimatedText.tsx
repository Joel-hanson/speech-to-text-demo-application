import { useEffect, useState } from 'react';


const AnimatedText = ({ text }: { text: string }) => {
    const [isTextVisible, setIsTextVisible] = useState(false);

    // Use useEffect to delay showing the text by a certain time
    useEffect(() => {
        const timeoutId = setTimeout(() => {
            setIsTextVisible(true);
        }, 600); // Delay time in milliseconds, e.g., 1000ms = 1 second

        // Clean up the timeout on unmount or when isTextVisible changes
        return () => {
            clearTimeout(timeoutId);
        };
    }, []);

    return (
        <div className="text-container mt-1 text-base leading-7 text-slate-700">
            {/* Use CSS transition to gradually reveal the text */}
            <span
                className={`animated-text ${isTextVisible ? 'text-visible' : ''}`}
            >
                {text ?
                    text.substring(0, 250) + (text.length > 250 ? "..." : "")
                    :
                    "Loading..."
                }

            </span>
        </div>
    );
};

export default AnimatedText;