import React, { useEffect, useState } from "react";

const TypedText: React.FC<{ text: string; delay: number }> = ({
    text,
    delay,
}) => {
    const [revealedLetters, setRevealedLetters] = useState(0);
    const interval = setInterval(() => setRevealedLetters((l) => l + 1), delay);

    useEffect(() => {
        if (revealedLetters === text.length) clearInterval(interval);
    }, [text, interval, revealedLetters]);

    useEffect(() => {
        return () => clearInterval(interval);
    }, [interval]);


    return <>{text.substring(0, revealedLetters)}</>
};

export default TypedText;
