<template>
  <div class="popup__comments flex column no-wrap q-ml-lg">
    <div class="comments__buttons flex">
      <q-btn
        class="comments__btn"
        size="sm"
        unelevated
        :color="
          kindFilter === 'all'
            ? 'accent'
            : kindFilter === 'log'
            ? 'secondary'
            : 'accent'
        "
        @click="toggleFilter('chat')"
      >
        <q-icon name="svguse:icons.svg#chat" color="white" size="12px" />
      </q-btn>
      <q-btn
        class="comments__btn"
        size="sm"
        unelevated
        :color="
          kindFilter === 'all'
            ? 'accent'
            : kindFilter === 'chat'
            ? 'secondary'
            : 'accent'
        "
        @click="toggleFilter('log')"
      >
        <q-icon name="svguse:icons.svg#clock" color="white" size="13px" />
      </q-btn>
      <q-btn
        class="comments__btn no-shadow"
        size="sm"
        unelevated
        text-color="accent"
        style="
          border-radius: 10px;
          width: 32px;
          height: 32px;
          background: rgba(56, 147, 147, 0.2);
        "
        @click="changeShowPopup"
      >
        <q-icon
          name="svguse:icons.min.svg#plus"
          style="transform: rotate(45deg)"
          size="14px"
        />
      </q-btn>
    </div>
    <span class="comments__title">Комментарии:</span>
    <div class="comments__main full-width full-height">
      <q-scroll-area style="height: 100%; max-width: 100%">
        <q-list>
          <template v-for="comment in filteredComments" :key="comment.id">
            <q-item v-if="comment">
              <p class="q-ma-none" v-if="comment.is_system_comment === true">
                <span class="text-accent"
                  >@{{ comment.created_by.first_name }}
                  {{ comment.created_by.last_name }}</span
                >
                {{ comment.text }}
              </p>
              <div class="flex no-wrap" v-else>
                <q-avatar class="comment__avatar q-mr-md" size="36px">
                  <q-img :src="comment.created_by.avatar" />
                </q-avatar>
                <div class="column">
                  <div class="comments__label">
                    <div class="comments__label">
                      <span class="comment__name">{{
                        comment.created_by.first_name
                      }}</span
                      >: {{ comment.text }}
                    </div>
                  </div>
                  <div class="comment__time">
                    {{ printDate(comment.created_at) }}
                  </div>
                </div>
              </div>
            </q-item>
          </template>
        </q-list>
      </q-scroll-area>
    </div>
    <div class="popup__comments-textarea q-mt-auto">
      <Textarea
        height="70px"
        v-model="comment"
        @add-comment="addComment"
        @get-caret="getCaretPosition"
      >
        <template v-slot:buttons>
          <q-icon
            name="svguse:icons.min.svg#tag"
            size="14px"
            color="grey"
            class="cursor-pointer"
          >
            <q-menu self="top middle" fit>
              <UserSelectList
                :users="users"
                @click-on-user-option="clickOnUserOption"
              />
            </q-menu>
          </q-icon>
          <q-icon
            name="svguse:icons.min.svg#smile"
            size="14px"
            color="grey"
            class="cursor-pointer"
          >
          </q-icon>
          <q-icon
            name="svguse:icons.min.svg#clip"
            size="14px"
            color="grey"
            class="cursor-pointer"
          >
            <input
              type="file"
              id="file"
              class="input__file cursor-pointer"
              ref="inputFile"
              @input="addFile"
            />
          </q-icon>
        </template>
        <template v-slot:enter>
          <q-btn class="btn__enter" unelevated size="sm" @click="addComment">
            <q-icon
              name="svguse:icons.min.svg#arrow_long_right_up"
              size="10px"
              color="white"
            />
          </q-btn>
        </template>
      </Textarea>
    </div>
  </div>
</template>

<script>
import { computed, ref } from 'vue';
import Textarea from 'components/ui/Textarea';
import { date } from 'quasar';
import { useStore } from 'vuex';
import UserSelectList from 'components/ui/UserSelectList';
export default {
  name: 'PopupComments',
  components: { UserSelectList, Textarea },
  props: {
    task: {
      type: Object,
      default: () => {},
    },
  },
  setup(props, { emit }) {
    const store = useStore();
    const comment = ref('');
    const caretPosition = ref(0);
    const filter = ref('all');
    const users = computed(() => store.getters['users/getUsers']);
    const kindFilter = computed(() => filter.value);
    const addFile = (evt) => {
      emit('addFile', {
        label: evt.target.files[0].name,
        date: date.formatDate(new Date(), 'MM/DD/YYYY, H:m a'),
      });
    };

    const filteredComments = computed(() => {
      if (kindFilter.value === 'chat') {
        return props.task.task_comments.filter(
          (item) => !item.is_system_comment
        );
      }
      if (kindFilter.value === 'log') {
        return props.task.task_comments.filter(
          (item) => item.is_system_comment
        );
      }

      return props.task.task_comments;
    });

    //TODO: Fix this
    const addComment = () => {
      emit('add-comment', comment.value.replace(/\s+/g, ' ').trim());
      comment.value = '';
    };

    const clickOnUserOption = (user) => {
      comment.value = comment.value + user.email;
    };

    const getCaretPosition = (position) => {
      caretPosition.value = position;
    };

    const changeShowPopup = () => {
      emit('changeShowPopup');
    };

    const printDate = (commentDate) => {
      return date.formatDate(new Date(commentDate), 'DD MMM HH:mm');
    };

    const toggleFilter = (val) => {
      if (filter.value === val) {
        filter.value = 'all';
      }

      filter.value = val;
    };

    return {
      comment,
      users,
      filter,
      filteredComments,
      kindFilter,
      addFile,
      addComment,
      clickOnUserOption,
      getCaretPosition,
      changeShowPopup,
      printDate,
      toggleFilter,
    };
  },
};
</script>

<style scoped lang="scss">
.comments {
  position: relative;
  &__title {
    font-size: 24px;
    font-weight: 600;
    color: $main-text;
  }
  &__btn {
    width: 32px;
    height: 32px;
    border-radius: 10px;
    margin-right: 15px;
    &:last-child {
      margin-right: 0;
    }
  }
  &__buttons {
    position: absolute;
    top: 10px;
    right: 10px;
  }
}
.comment {
  font-size: 14px;
  &__name {
    font-weight: 500;
  }
  &__time {
    color: rgba(183, 193, 208, 1);
  }
}
.input__file {
  position: absolute;
  content: '';
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  opacity: 0;
  cursor: pointer;
}
</style>
