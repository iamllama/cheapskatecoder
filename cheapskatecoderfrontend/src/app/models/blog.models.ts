export default class Blog {
    id: BigInteger;
    title: string;
    slug: string;
    blog_thumbnail: string;
    blog_banner_image: string;
    meta_summary: string;
    blog_content: string;
    author: string;
    series: [];
    categories: [];
    date_published: Date;
    username: string;
}