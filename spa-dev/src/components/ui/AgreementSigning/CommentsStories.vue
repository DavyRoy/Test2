<template>
  <div class="comments-stories">
    <div class="comment-story">
      <div class="com-stor-icons">
        <input class="input-icon1" type="radio" name="input" id="icon_1" />
        <label class="icon1" for="icon_1">
          <svg
            class="img2"
            width="13.5"
            height="13.5"
            viewBox="0 0 14 14"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M4.75 4.75H3.25V6.25H4.75V4.75Z" fill="#252733" />
            <path d="M6.25 4.75H7.75V6.25H6.25V4.75Z" fill="#252733" />
            <path d="M10.75 4.75H9.25V6.25H10.75V4.75Z" fill="#252733" />
            <path
              d="M0.25 1.75V13.75L3.85 11.05C4.10936 10.8547 4.42535 10.7494 4.75 10.75H12.25C13.0784 10.75 13.75 10.0784 13.75 9.25V1.75C13.75 0.921573 13.0784 0.25 12.25 0.25H1.75C0.921573 0.25 0.25 0.921573 0.25 1.75ZM1.75 10.75V1.75H12.25V9.25H4.2505C3.9258 9.24913 3.60973 9.35448 3.3505 9.55L1.75 10.75Z"
              fill="#252733"
            />
          </svg>
        </label>

        <input class="input-icon2" type="radio" name="input" id="icon_2" />
        <label class="icon2" for="icon_2"
          ><img
            class="img3"
            src="../../../../public/images/icontimeblack.png"
            alt=""
        /></label>

        <div class="com-title">
          <svg
            class="img1"
            width="13.5"
            height="13.5"
            viewBox="0 0 14 14"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M4.75 4.75H3.25V6.25H4.75V4.75Z" fill="#252733" />
            <path d="M6.25 4.75H7.75V6.25H6.25V4.75Z" fill="#252733" />
            <path d="M10.75 4.75H9.25V6.25H10.75V4.75Z" fill="#252733" />
            <path
              d="M0.25 1.75V13.75L3.85 11.05C4.10936 10.8547 4.42535 10.7494 4.75 10.75H12.25C13.0784 10.75 13.75 10.0784 13.75 9.25V1.75C13.75 0.921573 13.0784 0.25 12.25 0.25H1.75C0.921573 0.25 0.25 0.921573 0.25 1.75ZM1.75 10.75V1.75H12.25V9.25H4.2505C3.9258 9.24913 3.60973 9.35448 3.3505 9.55L1.75 10.75Z"
              fill="#252733"
            />
          </svg>
          <h1 class="com-h1">Комментарии:</h1>
        </div>
        <div class="stor-title">
          <img
            class="img1"
            src="../../../../public/images/icontimeblack.png"
            alt=""
          />
          <h1 class="com-h1">Истории:</h1>
        </div>

        <div class="comments">
          <div class="comment">
            <img class="ava-comment" src="Ellipse128.png" alt="" />
            <p class="name-comment">Никита:</p>
            <span class="comment-text"
              >Идейные соображения высшего порядка, а также дальнейшее развитие
              различных форм деятельности требуют</span
            >
            <br />
            <p class="time-comment">
              Согласновано 3 часа назад
              <button class="button-answer">Ответить</button>
            </p>
          </div>

          <div class="comment">
            <img class="ava-comment" src="Ellipse128.png" alt="" />
            <div class="comment-flex">
              <p class="name-comment">Никита:</p>
              <span class="comment-text"
                >Идейные соображения высшего порядка, а также дальнейшее
                развитие различных форм</span
              >
              <br />
              <p class="time-comment">
                Согласновано 3 часа назад
                <button class="button-answer">Ответить</button>
              </p>
            </div>
          </div>

          <hr class="comment-hr" />

          <div class="comment sub-comment">
            <img class="sub-ava-comment" src="Ellipse128.png" alt="" />
            <p class="name-comment">Никита:</p>
            <span class="comment-text"
              >Идейные соображения высшего порядка, а также дальнейшее</span
            >
            <br />
            <p class="time-comment">
              Согласновано 3 часа назад
              <button class="button-answer">Ответить</button>
            </p>
          </div>
          <div class="comment sub-comment">
            <img class="sub-ava-comment" src="Ellipse128.png" alt="" />
            <p class="name-comment">Никита:</p>
            <span class="comment-text"
              >Идейные соображения высшего порядка, а также дальнейшее развитие
              различных форм деятельности требуют</span
            >
            <br />
            <p class="time-comment">
              Согласновано 3 часа назад
              <button class="button-answer">Ответить</button>
            </p>
          </div>

          <div class="comment sub-comment">
            <img class="sub-ava-comment" src="Ellipse128.png" alt="" />
            <input
              placeholder="Ваш комментарий"
              class="comment-input"
              type="text"
            />
          </div>

          <div class="icons-area sub-icons-area">
            <button class="but-area sub-icons">
              <svg
                class="img4"
                width="10"
                height="10"
                viewBox="0 0 10 10"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M5.18942 10C4.36069 10 3.62405 9.88936 2.97948 9.66808C2.33754 9.44938 1.79558 9.12646 1.35359 8.69934C0.911602 8.2748 0.576164 7.75634 0.347277 7.14396C0.11839 6.53158 0.00263088 5.83173 0 5.04438C0.00263088 4.27505 0.119705 3.58163 0.351223 2.96411C0.582741 2.34401 0.92081 1.81397 1.36543 1.37399C1.81005 0.93143 2.35333 0.591792 2.99526 0.355076C3.6372 0.118359 4.36727 0 5.18548 0C5.95633 0 6.63904 0.114499 7.23362 0.343497C7.83083 0.572495 8.33465 0.891548 8.74507 1.30066C9.15812 1.70719 9.46988 2.1832 9.68035 2.72868C9.89345 3.27158 10 3.8608 10 4.49633C10 4.93632 9.9658 5.35315 9.8974 5.74682C9.82899 6.13791 9.71192 6.48527 9.54617 6.78888C9.38306 7.0925 9.16075 7.33436 8.87924 7.51447C8.59774 7.69201 8.2452 7.7885 7.82163 7.80394C7.55591 7.8168 7.32307 7.79236 7.12313 7.73061C6.92318 7.66885 6.76138 7.57237 6.63773 7.44114C6.51671 7.30735 6.44041 7.14396 6.40884 6.95098H6.36148C6.30097 7.10536 6.18653 7.24688 6.01815 7.37553C5.85241 7.50161 5.6472 7.60067 5.40253 7.67271C5.15785 7.74218 4.88556 7.77049 4.58564 7.75762C4.26467 7.74218 3.96738 7.67014 3.69376 7.54149C3.42278 7.41027 3.186 7.22758 2.98343 6.99344C2.78348 6.75672 2.62826 6.47112 2.51776 6.13663C2.40726 5.80214 2.35201 5.42262 2.35201 4.99807C2.35201 4.58382 2.41252 4.21845 2.53354 3.90197C2.65456 3.58549 2.81636 3.31532 3.01894 3.09147C3.22415 2.86762 3.45567 2.69265 3.7135 2.56658C3.97132 2.43793 4.23704 2.35559 4.51065 2.31957C4.79479 2.28097 5.06183 2.28483 5.31176 2.33115C5.56169 2.37746 5.76953 2.44822 5.93528 2.54342C6.10366 2.63862 6.20889 2.74283 6.25099 2.85604H6.30624V2.42377H7.40726V6.09803C7.40989 6.29101 7.45725 6.44667 7.54933 6.56503C7.64404 6.68339 7.77559 6.74257 7.94396 6.74257C8.15443 6.74257 8.32413 6.66152 8.45304 6.49942C8.58458 6.33475 8.67929 6.08259 8.73717 5.74296C8.79768 5.40075 8.82662 4.96333 8.82399 4.43072C8.82662 3.99331 8.76743 3.59707 8.64641 3.24199C8.52802 2.88434 8.35964 2.57044 8.14128 2.30027C7.92292 2.0301 7.66114 1.80497 7.35596 1.62486C7.05341 1.44217 6.71665 1.30452 6.3457 1.21189C5.97474 1.11926 5.57879 1.07295 5.15785 1.07295C4.51329 1.07295 3.94633 1.16943 3.45698 1.36241C2.96764 1.55281 2.55722 1.82426 2.22573 2.17677C1.89687 2.52927 1.64825 2.94738 1.47987 3.43111C1.31413 3.91226 1.23126 4.44487 1.23126 5.02895C1.23126 5.65419 1.31807 6.20867 1.49171 6.6924C1.66798 7.17355 1.92581 7.5788 2.26519 7.90814C2.60458 8.23749 3.0242 8.48707 3.52407 8.65689C4.02657 8.82671 4.60405 8.91162 5.25651 8.91162C5.55643 8.91162 5.84978 8.88846 6.13654 8.84215C6.42331 8.79583 6.68114 8.7418 6.91002 8.68005C7.13891 8.61829 7.31518 8.56426 7.43883 8.51795L7.77427 9.49826C7.61115 9.5806 7.39016 9.66036 7.11129 9.73755C6.83504 9.81474 6.52986 9.87778 6.19574 9.92667C5.86425 9.97556 5.52881 10 5.18942 10ZM4.91318 6.64994C5.2473 6.64994 5.51434 6.5869 5.71429 6.46083C5.91423 6.33218 6.05762 6.14177 6.14444 5.88962C6.23125 5.63746 6.27335 5.32356 6.27072 4.9479C6.27072 4.59797 6.22599 4.31108 6.13654 4.08722C6.04709 3.86337 5.90371 3.69741 5.70639 3.58935C5.50908 3.48128 5.2473 3.42725 4.92107 3.42725C4.62641 3.42725 4.37516 3.49286 4.16732 3.62408C3.96212 3.75531 3.80426 3.9367 3.69376 4.16827C3.5859 4.39727 3.53197 4.65843 3.53197 4.95176C3.53197 5.24508 3.57537 5.52168 3.66219 5.78155C3.75164 6.03885 3.89634 6.24855 4.09629 6.41065C4.29887 6.57018 4.57117 6.64994 4.91318 6.64994Z"
                  fill="#252733"
                />
              </svg>
            </button>
            <button class="but-area sub-icons">
              <svg
                class="img5"
                width="12"
                height="12"
                viewBox="0 0 12 12"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M5.99996 11.8332C2.7783 11.8332 0.166626 9.2215 0.166626 5.99984C0.166626 2.77818 2.7783 0.166504 5.99996 0.166504C9.22162 0.166504 11.8333 2.77818 11.8333 5.99984C11.8298 9.22003 9.22015 11.8296 5.99996 11.8332ZM5.99996 1.33317C3.42263 1.33317 1.33329 3.42251 1.33329 5.99984C1.33329 8.57717 3.42263 10.6665 5.99996 10.6665C8.57729 10.6665 10.6666 8.57717 10.6666 5.99984C10.6637 3.42371 8.57609 1.33606 5.99996 1.33317ZM5.99996 9.49984C5.07831 9.51544 4.20714 9.07985 3.66663 8.33317C3.40417 7.98218 3.20662 7.58707 3.08329 7.1665H8.91663C8.91663 7.1665 8.91663 7.1665 8.91663 7.17117C8.7914 7.58954 8.59398 7.9828 8.33329 8.33317C7.79271 9.07977 6.92159 9.51534 5.99996 9.49984ZM3.95829 5.99984C3.47504 5.99984 3.08329 5.60809 3.08329 5.12484C3.08329 4.64159 3.47504 4.24984 3.95829 4.24984C4.44154 4.24984 4.83329 4.64159 4.83329 5.12484C4.83329 5.60809 4.44154 5.99984 3.95829 5.99984ZM8.03754 5.99167C7.55655 5.99167 7.16663 5.60175 7.16663 5.12075C7.16663 4.63976 7.55655 4.24984 8.03754 4.24984C8.51854 4.24984 8.90846 4.63976 8.90846 5.12075C8.90782 5.60148 8.51827 5.99103 8.03754 5.99167Z"
                  fill="#252733"
                />
              </svg>
            </button>
            <button class="but-area sub-icons">
              <svg
                class="img6"
                width="9"
                height="10"
                viewBox="0 0 11 12"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M5.95348 1.98828L1.91655 5.86717C1.62597 6.14633 1.39548 6.47774 1.23821 6.8425C1.08095 7.20726 1 7.59821 1 7.99303C1 8.38786 1.08095 8.77882 1.23821 9.14358C1.39548 9.50834 1.62597 9.83976 1.91655 10.1189C2.20712 10.3981 2.55209 10.6196 2.93176 10.7707C3.31142 10.9218 3.71835 10.9996 4.1293 10.9996C4.54025 10.9996 4.94715 10.9218 5.32682 10.7707C5.70648 10.6196 6.05145 10.3981 6.34203 10.1189L9.35649 7.2225"
                  stroke="#252733"
                  stroke-width="1.2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                />
                <path
                  d="M3.60547 4.24557L6.35815 1.60068C6.55632 1.41024 6.79158 1.25918 7.05052 1.15612C7.30946 1.05305 7.58701 1 7.86729 1C8.14757 1 8.42509 1.05305 8.68403 1.15612C8.94297 1.25918 9.17825 1.41024 9.37643 1.60068V1.60068C9.77644 1.98529 10.0011 2.50677 10.0011 3.05051C10.0011 3.59424 9.77644 4.11573 9.37643 4.50034L6.62134 7.14617"
                  stroke="#252733"
                  stroke-width="1.2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                />
                <path
                  d="M6.36797 4.28125L3.52372 7.01415C3.30844 7.22114 3.1875 7.50178 3.1875 7.79441C3.1875 8.08704 3.30844 8.3677 3.52372 8.57469C3.63033 8.67722 3.75692 8.75856 3.89626 8.81406C4.0356 8.86956 4.18495 8.89813 4.33579 8.89813C4.48663 8.89813 4.63598 8.86956 4.77532 8.81406C4.91466 8.75856 5.04122 8.67722 5.14783 8.57469L6.62975 7.15126"
                  stroke="#252733"
                  stroke-width="1.2"
                  stroke-miterlimit="10"
                  stroke-linecap="round"
                />
              </svg>
            </button>
          </div>
        </div>

        <div class="stories">
          <div class="comment">
            <img class="ava-comment" src="Ellipse128.png" alt="" />
            <p class="name-comment">Никита</p>
            <span class="comment-text done">Согласовал</span>
            <br />
            <p class="time-comment">3 часа назад</p>
          </div>

          <div class="comment">
            <img class="ava-comment" src="Ellipse128.png" alt="" />
            <p class="name-comment">Никита</p>
            <span class="comment-text done">Делегировал</span>
            <br />
            <p class="time-comment">3 часа назад</p>
          </div>
          <div class="comment">
            <img class="ava-comment" src="Ellipse128.png" alt="" />
            <p class="name-comment">Никита</p>
            <span class="comment-text done">Согласовал</span>
            <br />
            <p class="time-comment">3 часа назад</p>
          </div>
        </div>
      </div>

      <div class="comment-area">
        <img class="ava-area" src="Ellipse128.png" alt="" />
        <textarea
          class="textarea"
          maxlength="3000"
          placeholder="Ваш комментарий"
          name=""
          id=""
          cols="30"
          rows="10"
        ></textarea>
        <div class="icons-area">
          <button class="but-area">
            <svg
              class="img4"
              width="10"
              height="10"
              viewBox="0 0 10 10"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M5.18942 10C4.36069 10 3.62405 9.88936 2.97948 9.66808C2.33754 9.44938 1.79558 9.12646 1.35359 8.69934C0.911602 8.2748 0.576164 7.75634 0.347277 7.14396C0.11839 6.53158 0.00263088 5.83173 0 5.04438C0.00263088 4.27505 0.119705 3.58163 0.351223 2.96411C0.582741 2.34401 0.92081 1.81397 1.36543 1.37399C1.81005 0.93143 2.35333 0.591792 2.99526 0.355076C3.6372 0.118359 4.36727 0 5.18548 0C5.95633 0 6.63904 0.114499 7.23362 0.343497C7.83083 0.572495 8.33465 0.891548 8.74507 1.30066C9.15812 1.70719 9.46988 2.1832 9.68035 2.72868C9.89345 3.27158 10 3.8608 10 4.49633C10 4.93632 9.9658 5.35315 9.8974 5.74682C9.82899 6.13791 9.71192 6.48527 9.54617 6.78888C9.38306 7.0925 9.16075 7.33436 8.87924 7.51447C8.59774 7.69201 8.2452 7.7885 7.82163 7.80394C7.55591 7.8168 7.32307 7.79236 7.12313 7.73061C6.92318 7.66885 6.76138 7.57237 6.63773 7.44114C6.51671 7.30735 6.44041 7.14396 6.40884 6.95098H6.36148C6.30097 7.10536 6.18653 7.24688 6.01815 7.37553C5.85241 7.50161 5.6472 7.60067 5.40253 7.67271C5.15785 7.74218 4.88556 7.77049 4.58564 7.75762C4.26467 7.74218 3.96738 7.67014 3.69376 7.54149C3.42278 7.41027 3.186 7.22758 2.98343 6.99344C2.78348 6.75672 2.62826 6.47112 2.51776 6.13663C2.40726 5.80214 2.35201 5.42262 2.35201 4.99807C2.35201 4.58382 2.41252 4.21845 2.53354 3.90197C2.65456 3.58549 2.81636 3.31532 3.01894 3.09147C3.22415 2.86762 3.45567 2.69265 3.7135 2.56658C3.97132 2.43793 4.23704 2.35559 4.51065 2.31957C4.79479 2.28097 5.06183 2.28483 5.31176 2.33115C5.56169 2.37746 5.76953 2.44822 5.93528 2.54342C6.10366 2.63862 6.20889 2.74283 6.25099 2.85604H6.30624V2.42377H7.40726V6.09803C7.40989 6.29101 7.45725 6.44667 7.54933 6.56503C7.64404 6.68339 7.77559 6.74257 7.94396 6.74257C8.15443 6.74257 8.32413 6.66152 8.45304 6.49942C8.58458 6.33475 8.67929 6.08259 8.73717 5.74296C8.79768 5.40075 8.82662 4.96333 8.82399 4.43072C8.82662 3.99331 8.76743 3.59707 8.64641 3.24199C8.52802 2.88434 8.35964 2.57044 8.14128 2.30027C7.92292 2.0301 7.66114 1.80497 7.35596 1.62486C7.05341 1.44217 6.71665 1.30452 6.3457 1.21189C5.97474 1.11926 5.57879 1.07295 5.15785 1.07295C4.51329 1.07295 3.94633 1.16943 3.45698 1.36241C2.96764 1.55281 2.55722 1.82426 2.22573 2.17677C1.89687 2.52927 1.64825 2.94738 1.47987 3.43111C1.31413 3.91226 1.23126 4.44487 1.23126 5.02895C1.23126 5.65419 1.31807 6.20867 1.49171 6.6924C1.66798 7.17355 1.92581 7.5788 2.26519 7.90814C2.60458 8.23749 3.0242 8.48707 3.52407 8.65689C4.02657 8.82671 4.60405 8.91162 5.25651 8.91162C5.55643 8.91162 5.84978 8.88846 6.13654 8.84215C6.42331 8.79583 6.68114 8.7418 6.91002 8.68005C7.13891 8.61829 7.31518 8.56426 7.43883 8.51795L7.77427 9.49826C7.61115 9.5806 7.39016 9.66036 7.11129 9.73755C6.83504 9.81474 6.52986 9.87778 6.19574 9.92667C5.86425 9.97556 5.52881 10 5.18942 10ZM4.91318 6.64994C5.2473 6.64994 5.51434 6.5869 5.71429 6.46083C5.91423 6.33218 6.05762 6.14177 6.14444 5.88962C6.23125 5.63746 6.27335 5.32356 6.27072 4.9479C6.27072 4.59797 6.22599 4.31108 6.13654 4.08722C6.04709 3.86337 5.90371 3.69741 5.70639 3.58935C5.50908 3.48128 5.2473 3.42725 4.92107 3.42725C4.62641 3.42725 4.37516 3.49286 4.16732 3.62408C3.96212 3.75531 3.80426 3.9367 3.69376 4.16827C3.5859 4.39727 3.53197 4.65843 3.53197 4.95176C3.53197 5.24508 3.57537 5.52168 3.66219 5.78155C3.75164 6.03885 3.89634 6.24855 4.09629 6.41065C4.29887 6.57018 4.57117 6.64994 4.91318 6.64994Z"
                fill="#252733"
              />
            </svg>
          </button>
          <button class="but-area">
            <svg
              class="img5"
              width="12"
              height="12"
              viewBox="0 0 12 12"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M5.99996 11.8332C2.7783 11.8332 0.166626 9.2215 0.166626 5.99984C0.166626 2.77818 2.7783 0.166504 5.99996 0.166504C9.22162 0.166504 11.8333 2.77818 11.8333 5.99984C11.8298 9.22003 9.22015 11.8296 5.99996 11.8332ZM5.99996 1.33317C3.42263 1.33317 1.33329 3.42251 1.33329 5.99984C1.33329 8.57717 3.42263 10.6665 5.99996 10.6665C8.57729 10.6665 10.6666 8.57717 10.6666 5.99984C10.6637 3.42371 8.57609 1.33606 5.99996 1.33317ZM5.99996 9.49984C5.07831 9.51544 4.20714 9.07985 3.66663 8.33317C3.40417 7.98218 3.20662 7.58707 3.08329 7.1665H8.91663C8.91663 7.1665 8.91663 7.1665 8.91663 7.17117C8.7914 7.58954 8.59398 7.9828 8.33329 8.33317C7.79271 9.07977 6.92159 9.51534 5.99996 9.49984ZM3.95829 5.99984C3.47504 5.99984 3.08329 5.60809 3.08329 5.12484C3.08329 4.64159 3.47504 4.24984 3.95829 4.24984C4.44154 4.24984 4.83329 4.64159 4.83329 5.12484C4.83329 5.60809 4.44154 5.99984 3.95829 5.99984ZM8.03754 5.99167C7.55655 5.99167 7.16663 5.60175 7.16663 5.12075C7.16663 4.63976 7.55655 4.24984 8.03754 4.24984C8.51854 4.24984 8.90846 4.63976 8.90846 5.12075C8.90782 5.60148 8.51827 5.99103 8.03754 5.99167Z"
                fill="#252733"
              />
            </svg>
          </button>
          <button class="but-area">
            <svg
              class="img6"
              width="9"
              height="10"
              viewBox="0 0 11 12"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M5.95348 1.98828L1.91655 5.86717C1.62597 6.14633 1.39548 6.47774 1.23821 6.8425C1.08095 7.20726 1 7.59821 1 7.99303C1 8.38786 1.08095 8.77882 1.23821 9.14358C1.39548 9.50834 1.62597 9.83976 1.91655 10.1189C2.20712 10.3981 2.55209 10.6196 2.93176 10.7707C3.31142 10.9218 3.71835 10.9996 4.1293 10.9996C4.54025 10.9996 4.94715 10.9218 5.32682 10.7707C5.70648 10.6196 6.05145 10.3981 6.34203 10.1189L9.35649 7.2225"
                stroke="#252733"
                stroke-width="1.2"
                stroke-miterlimit="10"
                stroke-linecap="round"
              />
              <path
                d="M3.60547 4.24557L6.35815 1.60068C6.55632 1.41024 6.79158 1.25918 7.05052 1.15612C7.30946 1.05305 7.58701 1 7.86729 1C8.14757 1 8.42509 1.05305 8.68403 1.15612C8.94297 1.25918 9.17825 1.41024 9.37643 1.60068V1.60068C9.77644 1.98529 10.0011 2.50677 10.0011 3.05051C10.0011 3.59424 9.77644 4.11573 9.37643 4.50034L6.62134 7.14617"
                stroke="#252733"
                stroke-width="1.2"
                stroke-miterlimit="10"
                stroke-linecap="round"
              />
              <path
                d="M6.36797 4.28125L3.52372 7.01415C3.30844 7.22114 3.1875 7.50178 3.1875 7.79441C3.1875 8.08704 3.30844 8.3677 3.52372 8.57469C3.63033 8.67722 3.75692 8.75856 3.89626 8.81406C4.0356 8.86956 4.18495 8.89813 4.33579 8.89813C4.48663 8.89813 4.63598 8.86956 4.77532 8.81406C4.91466 8.75856 5.04122 8.67722 5.14783 8.57469L6.62975 7.15126"
                stroke="#252733"
                stroke-width="1.2"
                stroke-miterlimit="10"
                stroke-linecap="round"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.ava-comment {
  flex: 46;
}
.comment-flex {
  flex: 837;
}

div {
  box-sizing: border-box;
}

.comments-stories {
  height: 383px;
  position: relative;
}

.comment-story {
  height: 281px;
}

.com-title {
  display: flex;
  position: absolute;
  right: 880px;
}

.stor-title {
  display: none;
  position: absolute;
  right: 880px;
}

.img1 {
  width: 13.5px;
  height: 13.5px;
  position: absolute;
  top: 7px;
  left: 2px;
}

.com-h1 {
  font-family: Inter;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  position: absolute;
  top: 5px;
  left: 23px;
  margin: 0;
}

.com-stor-icons {
  display: flex;
  position: absolute;
  top: 10px;
  right: 0;
  height: 32px;
  width: 80px;
  justify-content: space-between;
}

.input-icon1,
.input-icon2 {
  appearance: none;
  -webkit-appearance: none;
  position: absolute;
  height: 0;
  width: 0;
}

.icon:hover {
  background-color: #389393;
}

.icon1 {
  cursor: pointer;
  display: block;
  flex: 1;
  max-width: 32px;
  height: 32px;
  box-sizing: border-box;
  background: #eef0f5;
  border-radius: 10px;
  position: relative;
}

.icon2 {
  cursor: pointer;
  display: block;
  flex: 1;
  max-width: 32px;
  height: 32px;
  box-sizing: border-box;
  background: #eef0f5;
  border-radius: 10px;
  position: relative;
}

.img2 {
  width: 12px;
  height: 12px;
  position: absolute;
  top: 10px;
  left: 10px;
}

.img3 {
  width: 13px;
  height: 13px;
  position: absolute;
  top: 9px;
  left: 9px;
}

.comments {
  width: 884px;
  height: 234px;
  position: absolute;
  top: 43px;
  right: 0px;
  display: block;
}

.input-icon1:checked ~ .comments {
  display: block;
}

.input-icon2:checked ~ .stories {
  display: block;
}

.input-icon2:checked ~ .comments {
  display: none;
}

.input-icon2:checked ~ .stor-title {
  display: block;
}

.input-icon2:checked ~ .com-title {
  display: none;
}

.input-icon1:checked ~ .com-title {
  display: block;
}

.input-icon1:checked ~ .icon1 {
  background-color: #389393;
}

.input-icon2:checked ~ .icon2 {
  background-color: #389393;
}

.stories {
  width: 884px;
  height: 138px;
  position: absolute;
  top: 43px;
  right: 0px;
  display: none;
}

.comment-text {
  font-family: Inter;
  font-size: 12px;
  font-weight: 300;
  line-height: 15px;
  position: absolute;
  left: 96px;
  top: 3px;
}

.done {
  color: #389393;
  left: 150px;
  top: 7px;
  border: 1px solid #389393;
  padding: 4px 8px;
  border-radius: 5px;
}

.comment-hr {
  transform: rotate(180deg);
  position: absolute;
  left: 17px;
  height: 70px;
  border: 0.5px solid rgba(236, 236, 236, 1);
}

input::-webkit-input-placeholder {
  color: rgba(159, 162, 180, 1);
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
}

.comment-input {
  width: 790px;
  height: 30px;
  border-radius: 0px 10px 10px 10px;
  background-color: rgba(240, 242, 245, 1);
  border: none;
  margin-left: 45px;
  box-sizing: border-box;
  padding: 10px;
}

.comment {
  display: flex;
  height: 36px;
  margin-bottom: 15px;
  position: relative;
}

.sub-comment {
  left: 30px;
}

.ava-comment {
  height: 36px;
  width: 36px;
  position: absolute;
  top: -2px;
}

.sub-ava-comment {
  width: 24px;
  height: 24px;
  left: 14px;
  position: absolute;
  top: 2px;
}

.name-comment {
  font-family: 'Inter';
  font-size: 12px;
  font-weight: 500;
  line-height: 15px;
  position: absolute;
  top: 3px;
  left: 46px;
  margin: 0;
}

.time-comment {
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  color: #b7c1d0;
  position: absolute;
  left: 46px;
  bottom: 3px;
  margin: 0;
}

.button-answer {
  font-family: Inter;
  font-size: 12px;
  font-weight: 500;
  line-height: 15px;
  color: rgba(148, 148, 148, 1);
  height: 15px;
  width: 56px;
  border: none;
  background-color: white;
}

.ava-area {
  position: absolute;
  top: 30px;
  left: 0;
  width: 35px;
  height: 35px;
}

.comment-area {
  width: 863px;
  display: flex;
  height: 100px;
  position: absolute;
  top: 277px;
}

.textarea {
  width: 818px;
  height: 70px;
  position: absolute;
  left: 46px;
  bottom: 0px;
  box-sizing: border-box;
  font-family: Inter;
  font-size: 12px;
  font-weight: 400;
  line-height: 15px;
  color: #b7c1d0;
  border: 1px solid #e8ebf0;
  border-radius: 0px 10px 10px 10px;
  resize: none;
}

.but-area {
  max-height: 14px;
  border: none;
  background-color: white;
}

.icons-area {
  position: absolute;
  right: 10px;
  bottom: 10px;
  height: 14px;
  width: 47px;
  display: flex;
  justify-content: space-between;
}

.sub-icons-area {
  position: absolute;
  bottom: 8px;
  right: 30px;
}

.sub-icons {
  background-color: rgba(240, 242, 245, 1);
}

.img4 {
  height: 10px;
  width: 10px;
  position: absolute;
  left: 2px;
  top: 2px;
}

.img5 {
  height: 11.67px;
  width: 11.67px;
  position: absolute;
  top: 1.165px;
  left: 18.17px;
}

.img6 {
  width: 9px;
  height: 10px;
  position: absolute;
  top: 2px;
  right: 2px;
}

.button-link {
  height: 102px;
  position: relative;
  top: 93px;
}

.buttons {
  height: 50px;
  position: absolute;
  top: 30px;
  left: 0;
  justify-content: space-between;
}

button {
  cursor: pointer;
}

.com-stor-button {
  box-sizing: border-box;
  width: 155px;
  height: 50px;
  padding: 16px, 21px, 16px, 21px;
  border-radius: 10px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 500;
  line-height: 17px;
  cursor: pointer;
  margin-right: 10px;
}

.do {
  background-color: #eef0f5;
  border: 1px solid #eef0f5;
  color: rgba(0, 0, 0, 0.2);
}

.undo {
  border: 1px solid #f66161;
  color: #f66161;
  background-color: white;
}

.deleg {
  border: 1px solid #389393;
  color: #389393;
  background-color: white;
}

.links {
  height: 32px;
  display: flex;
  justify-content: space-between;
  position: absolute;
  top: 30px;
  right: 7px;
}

.link {
  width: 32px;
  height: 32px;
  border-radius: 10px;
  border: 1px solid #b7c1d0;
  position: relative;
  background-color: white;
}

.img7 {
  height: 12px;
  width: 12px;
  position: absolute;
  top: 9px;
  left: 9px;
}

.img8 {
  height: 14px;
  width: 14px;
  position: absolute;
  top: 8px;
  left: 8px;
}

.img9 {
  height: 15px;
  width: 12px;
  position: absolute;
  top: 7px;
  left: 9px;
}

.img10 {
  height: 12px;
  width: 15px;
  position: absolute;
  top: 9px;
  left: 7px;
}

.img11 {
  height: 13.5px;
  width: 15px;
  position: absolute;
  top: 8.5px;
  left: 7px;
}

.img12 {
  height: 15px;
  width: 13.5px;
  position: absolute;
  top: 7px;
  left: 8px;
}

.link-delete1 {
  display: none;
  position: absolute;
  right: 216px;
  top: 31px;
  height: 30px;
  width: 93px;
  border-radius: 4px;
  background-color: black;
  color: white;
  box-sizing: border-box;
  text-align: center;
  padding: 5px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
}

.link-delete1::after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0px 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: -5px;
  right: 80px;
  transform: rotate(180deg);
}

.tooltip1:hover + .link-delete1 {
  display: block;
}

.link-delete2 {
  display: none;
  position: absolute;
  right: 167px;
  top: 31px;
  height: 30px;
  width: 85px;
  border-radius: 4px;
  background-color: black;
  color: white;
  box-sizing: border-box;
  text-align: center;
  padding: 5px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
}

.link-delete2::after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0px 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: -5px;
  right: 72px;
  transform: rotate(180deg);
}

.tooltip2:hover + .link-delete2 {
  display: block;
}

.link-delete3 {
  display: none;
  position: absolute;
  right: 110px;
  top: 31px;
  height: 30px;
  width: 85px;
  border-radius: 4px;
  background-color: black;
  color: white;
  box-sizing: border-box;
  text-align: center;
  padding: 5px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
}

.link-delete3::after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0px 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: -5px;
  right: 72px;
  transform: rotate(180deg);
}

.tooltip3:hover + .link-delete3 {
  display: block;
}

.link-delete4 {
  display: none;
  position: absolute;
  right: 53px;
  top: 31px;
  height: 30px;
  width: 85px;
  border-radius: 4px;
  background-color: black;
  color: white;
  box-sizing: border-box;
  text-align: center;
  padding: 5px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
}

.link-delete4::after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0px 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: -5px;
  right: 72px;
  transform: rotate(180deg);
}

.tooltip4:hover + .link-delete4 {
  display: block;
}

.link-delete5 {
  display: none;
  position: absolute;
  right: -4px;
  top: 31px;
  height: 30px;
  width: 85px;
  border-radius: 4px;
  background-color: black;
  color: white;
  box-sizing: border-box;
  text-align: center;
  padding: 5px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
}

.link-delete5::after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0px 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: -5px;
  right: 72px;
  transform: rotate(180deg);
}

.tooltip5:hover + .link-delete5 {
  display: block;
}

.link-delete6 {
  display: none;
  position: absolute;
  right: -61px;
  top: 31px;
  height: 30px;
  width: 85px;
  border-radius: 4px;
  background-color: black;
  color: white;
  box-sizing: border-box;
  text-align: center;
  padding: 5px;
  font-family: Inter;
  font-size: 14px;
  font-weight: 600;
  line-height: 20px;
}

.link-delete6::after {
  content: '';
  display: block;
  border-style: solid;
  border-width: 5px 5px 0px 5px;
  border-color: black transparent transparent transparent;
  position: absolute;
  top: -5px;
  right: 72px;
  transform: rotate(180deg);
}

.tooltip6:hover + .link-delete6 {
  display: block;
}
</style>
