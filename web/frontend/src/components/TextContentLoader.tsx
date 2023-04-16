import ContentLoader from "react-content-loader";

const TextContentLoader = (props: JSX.IntrinsicAttributes) => (
    <ContentLoader
        speed={4}
        width={650}
        height={84}
        viewBox="0 0 650 84"
        backgroundColor="#f3f3f3"
        foregroundColor="#ecebeb"
        {...props}
    >
        <rect x="0" y="10" rx="3" ry="3" width="650" height="9" />
        <rect x="0" y="36" rx="3" ry="3" width="650" height="9" />
        <rect x="0" y="66" rx="3" ry="3" width="650" height="9" />
    </ContentLoader>
)

export default TextContentLoader;