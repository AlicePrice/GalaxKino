from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def header_all_pages():
	return mark_safe('''<head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <title>Галакс</title>
        <!-- Bootstrap -->
        <link href="/static/bootstrap/css/bootstrap.css" rel="stylesheet" type="text/css" />
        <!-- Animate.css -->
        <link href="/static/animate.css/animate.css" rel="stylesheet" type="text/css" />
        <!-- Font Awesome iconic font -->
        <link href="/static/fontawesome/css/fontawesome-all.css" rel="stylesheet" type="text/css" />
        <!-- Magnific Popup -->
        <link href="/static/magnific-popup/magnific-popup.css" rel="stylesheet" type="text/css" />
        <!-- Slick carousel -->
        <link href="/static/slick/slick.css" rel="stylesheet" type="text/css" />
        <!-- Fonts -->
        <link href='https://fonts.googleapis.com/css?family=Oswald:300,400,500,700' rel='stylesheet' type='text/css'>
        <link href='https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700' rel='stylesheet' type='text/css'>
        <!-- Theme styles -->
        <link href="/static/css/dot-icons.css" rel="stylesheet" type="text/css">
        <link href="/static/css/theme.css" rel="stylesheet" type="text/css">
    </head>
    <body class="body">
        <header class="header header-horizontal header-view-pannel">
            <div class="container">
                <nav class="navbar">
                    <a class="navbar-brand" href="/">
                        <span class="logo-element">
                            <span class="logo-tape">
                                <span class="svg-content svg-fill-theme" data-svg="./images/svg/logo-part.svg"></span>
                            </span>
                            <span class="logo-text text-uppercase">
                                Галакс</span>
                        </span>
                    </a>
                    <button class="navbar-toggler" type="button">
                        <span class="th-dots-active-close th-dots th-bars">
                            <span></span>
                            <span></span>
                            <span></span>
                        </span>
                    </button>
                    <div class="navbar-collapse">
                        <ul class="navbar-nav">
                            <li class="nav-item nav-item-arrow-down nav-hover-show-sub">
                                <a class="nav-link" href="#">Афиша</a>
                            </li>
                            <li class="nav-item nav-item-arrow-down nav-hover-show-sub" href="/scheme/">
                                <a class="nav-link" href="/scheme/">Схема залов и цены</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="movies-blocks.html">Акции</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="contact-us.html">Контакты</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="contact-us.html">Реклама</a>
                            </li>
                            <li class="nav-item nav-item-arrow-down nav-hover-show-sub">
                                <a class="nav-link" href="#" data-role="nav-toggler">Аккаунт</a>
                                        <div class="nav-arrow"><i class="fas fa-chevron-down"></i></div>
                                        <ul class="collapse nav">
                                            <li class="nav-item">
                                                <a class="nav-link" href="sign-in.html">Вход</a>
                                            </li>
                                            <li class="nav-item">
                                                <a class="nav-link" href="sign-up.html">Регистрация</a>
                                            </li>
                                        </ul>
                                    </li>
                            </li>
                        </ul>
                        <div class="navbar-extra">
                            <a class="btn-theme btn" href="#"><i class="fas fa-ticket-alt"></i>&nbsp;&nbsp;Купить билет</a>
                        </div>
                    </div>
                </nav>
            </div>
        </header>''')


@register.simple_tag
def footer_all_pages():
	return mark_safe('''<footer class="section-text-white footer footer-links bg-darken">
            <div class="footer-body container">
                <div class="row">
                    <div class="col-sm-6 col-lg-3">
                        <a class="footer-logo" href="/static/">
                            <span class="logo-element">
                                <span class="logo-text text-uppercase">
                                    Галакс</span>
                            </span>
                        </a>
                        <div class="footer-content">
                            <p class="footer-text">Sidestate NSW 4132,
                                <br/>Долгопрудный</p>
                            <p class="footer-text">Телефон:&nbsp;&nbsp;8(495)746-79-80</p>
                        </div>
                    </div>
                    <div class="col-sm-6 col-lg-3">
                        <h5 class="footer-title text-uppercase">Фильмы</h5>
                        <ul class="list-unstyled list-wide footer-content">
                            <li>
                                <a class="content-link" href="#">Все фильмы</a>
                            </li>
                            <li>
                                <a class="content-link" href="#">Summer movies collection</a>
                            </li>
                            <li>
                                <a class="content-link" href="#">Movie trailers</a>
                            </li>
                        </ul>
                    </div>
                    <div class="col-sm-6 col-lg-3">
                        <h5 class="footer-title text-uppercase">Информация</h5>
                        <ul class="list-unstyled list-wide footer-content">
                            <li>
                                <a class="content-link" href="#">Новости</a>
                            </li>
                            <li>
                                <a class="content-link" href="#">Контакты</a>
                            </li>
                            <li>
                                <a class="content-link" href="#">Сообщество</a>
                            </li>
                            <li>
                                <a class="content-link" href="#">События</a>
                            </li>
                            <li>
                                <a class="content-link" href="#">Помощь</a>
                            </li>
                        </ul>
                    </div>
                    <div class="col-sm-6 col-lg-3">
                        <h5 class="footer-title text-uppercase">Мы также в</h5>
                        <ul class="list-wide footer-content list-inline">
                            <li class="list-inline-item">
                                <a class="content-link" href="#"><i class="fab fa-slack-hash"></i></a>
                            </li>
                            <li class="list-inline-item">
                                <a class="content-link" href="#"><i class="fab fa-twitter"></i></a>
                            </li>
                            <li class="list-inline-item">
                                <a class="content-link" href="#"><i class="fab fa-facebook-f"></i></a>
                            </li>
                            <li class="list-inline-item">
                                <a class="content-link" href="#"><i class="fab fa-dribbble"></i></a>
                            </li>
                            <li class="list-inline-item">
                                <a class="content-link" href="#"><i class="fab fa-google-plus-g"></i></a>
                            </li>
                            <li class="list-inline-item">
                                <a class="content-link" href="#"><i class="fab fa-instagram"></i></a>
                            </li>
                        </ul>
                        <h5 class="footer-title text-uppercase">Подписаться</h5>
                        <div class="footer-content">
                            <p class="footer-text">Получайте новости о последних новинках</p>
                            <form class="footer-form" autocomplete="off">
                                <div class="input-group">
                                    <input class="form-control" name="email" type="email" placeholder="Email" />
                                    <div class="input-group-append">
                                        <button class="btn btn-theme" type="submit"><i class="fas fa-angle-right"></i></button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <div class="footer-copy">
                <div class="container">Copyright 2021 &copy; ООО Галакс кино. All rights reserved.</div>
            </div>
        </footer>
        <!-- jQuery library -->
        <script src="/static/js/jquery-3.3.1.js"></script>
        <!-- Bootstrap -->
        <script src="/static/bootstrap/js/bootstrap.js"></script>
        <!-- Paralax.js -->
        <script src="/static/parallax.js/parallax.js"></script>
        <!-- Waypoints -->
        <script src="/static/waypoints/jquery.waypoints.min.js"></script>
        <!-- Slick carousel -->
        <script src="/static/slick/slick.min.js"></script>
        <!-- Magnific Popup -->
        <script src="/static/magnific-popup/jquery.magnific-popup.min.js"></script>
        <!-- Inits product scripts -->
        <script src="/static/js/script.js"></script>
        <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAJ4Qy67ZAILavdLyYV2ZwlShd0VAqzRXA&callback=initMap"></script>
        <script async defer src="https://ia.media-imdb.com/images/G/01/imdb/plugins/rating/js/rating.js"></script>
    </body>
</html>
''')

