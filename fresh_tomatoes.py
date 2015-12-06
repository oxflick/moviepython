import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        .navbar-inverse {
            background-image: linear-gradient(to bottom,#4A1942 0,#893168 80%);
            border-color: #893168;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        .navbar-brand {
            width: 96px;
            margin-top: 10px;
            background: url('data:image/png;base64,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')
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        h2 {
            color: #4A1942;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#"></a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <p>{movie_actors}</p>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_actors=movie.actors,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)