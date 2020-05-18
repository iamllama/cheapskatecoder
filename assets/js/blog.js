$(document).ready(() => {
    $.ajax({
        url: 'http://localhost:55403/api/v1/blog',
        type: 'get',
        success: (res) => {
            for (let blog of res) {
                $("#blog-cards").append(
                    `
                    <div class="col-md-12 col-lg-4">
                        <div class="card" style="width: 18rem;">
                            <div class="card-body">
                                <h5 class="card-title">${blog.title}</h5>
                                <p class="card-text">${blog.meta_summary.substring(0, 200)} <span id="read-more"><a href="#">read more...</a></span></p>
                                <a href="#" class="card-link">Card link</a>
                                <a href="#" class="card-link">Another link</a>
                            </div>
                        </div>
                    </div>
                    `
                )
            }
        },
        error: (err) => {
            console.log(err);
        },
    })
});