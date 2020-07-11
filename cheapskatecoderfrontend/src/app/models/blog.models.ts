export default class Blog {
    id: number;
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
    author_profile_photo: string;
    author_full_name: string;
}