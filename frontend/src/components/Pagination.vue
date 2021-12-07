<template>
  <div class="pagination">
    <div class="pagination__container">
      <b-iconstack
        rotate="180"
        font-scale="1.75"
        class="pagination__arrow"
        @click="prevPage"
        :class="currPage > 0 ? '' : 'pagination__arrow--disabled'"
      >
        <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
        <b-icon stacked icon="circle"></b-icon>
        <b-icon stacked icon="chevron-right"></b-icon>
      </b-iconstack>
      <span class="pagination__page">{{ currPage + 1 }}</span>
      <b-iconstack
        font-scale="1.75"
        class="pagination__arrow"
        @click="nextPage"
        :class="currPage < pages - 1 ? '' : 'pagination__arrow--disabled'"
      >
        <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
        <b-icon stacked icon="circle"></b-icon>
        <b-icon stacked icon="chevron-right"></b-icon>
      </b-iconstack>
    </div>
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

  props: {
    pages: {
      type: Number,
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
      if (this.currPage > 0) {
        this.currPage -= 1;
      }
    },

    nextPage() {
      if (this.currPage < this.pages - 1) {
        this.currPage += 1;
      }
    },
  },
};
</script>

<style lang="scss">
.pagination {
  width: max-content;
  margin-top: -3px;
  &__page {
    font-size: 32px;
    margin-left: 5px;
    margin-right: 5px;
  }

  &__container {
    display: flex;
    align-items: center;
    border: 3px solid black;
    background-color: $gray-400;
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
</style>
