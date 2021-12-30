<template>
  <div class="pagination w-100">
    <button
      class="pagination__button"
      @click="prevPage"
      :disabled="!canGoBack"
      :class="!canGoBack ? 'pagination__button--disabled' : ''"
    >
      Til baka
    </button>
    <div class="year-selector">
      <b-form-select
        plain
        :value="$store.year"
        @change="updateYear"
        :options="$store.years"
      />
    </div>
    <button
      class="pagination__button"
      :class="!canGoNext ? 'pagination__button--disabled' : ''"
      :disabled="!canGoNext"
      @click="nextPage"
    >
      Áfram
    </button>
  </div>
</template>

<script>
export default {
  name: "Pagination",

  data() {
    return {
      fetching: false,
      currPage: 0,
    };
  },

  computed: {
    canGoBack() {
      return this.btnPage || this.currPage > 0;
    },
    canGoNext() {
      return !this.btnPage || this.currPage < this.pages - 1;
    },
  },

  props: {
    pages: {
      type: Number,
      required: true,
    },
    btnPage: {
      type: Boolean,
      required: true,
    },
  },

  watch: {
    currPage() {
      this.$emit("navigate", this.currPage);
    },
  },

  methods: {
    prevPage() {
      if (this.btnPage) {
        this.$emit("clear");
        return;
      }
      if (this.currPage > 0) {
        this.currPage -= 1;
      }
    },

    nextPage() {
      if (this.currPage < this.pages - 1) {
        this.currPage += 1;
      }
    },
    updateYear(year) {
      this.$emit("update", year);
    },
  },
};
</script>

<style lang="scss">
.pagination {
  margin-top: -3px;
  display: flex;
  background-color: rgba(black, 0.2);
  border-radius: 20px;
  padding: 5px;
  align-items: center;
  justify-content: space-between;

  &__button {
    color: white;
    background-color: #242424;
    border: none;
    border-radius: 35px;
    width: 200px;
    height: 35px;
    &--disabled {
      opacity: 0.7;
    }
  }

  &__container {
    padding-left: 5px;
    padding-right: 5px;
  }

  &__arrow {
    cursor: pointer;
    &--disabled {
      cursor: auto;
      opacity: 0.75;
    }

    &:hover {
      opacity: 0.75;
      transition: opacity 0.3s ease;
    }
  }
}
.year-selector {
  select {
    background-color: #242424;
    color: white;
    font-size: 18px;
    border-radius: 35px;
    border: none;
    width: 100px;
    appearance: none;
    text-align: center;
    &:focus {
      background-color: #242424;
      color: white;
    }
  }
  select.form-control {
    height: 35px !important;
  }
}
</style>
