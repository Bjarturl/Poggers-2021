<template>
  <b-container class="character-creation__container">
    <b-row class="character">
      <div class="character__selection">
        <b-iconstack
          rotate="180"
          font-scale="1.75"
          class="pagination__arrow"
          @click="prev('base')"
        >
          <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
          <b-icon stacked icon="circle"></b-icon>
          <b-icon stacked icon="chevron-right"></b-icon>
        </b-iconstack>
        <b-iconstack
          rotate="180"
          font-scale="1.75"
          class="pagination__arrow"
          @click="prev('augu')"
        >
          <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
          <b-icon stacked icon="circle"></b-icon>
          <b-icon stacked icon="chevron-right"></b-icon>
        </b-iconstack>
        <b-iconstack
          rotate="180"
          font-scale="1.75"
          class="pagination__arrow"
          @click="prev('munnur')"
        >
          <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
          <b-icon stacked icon="circle"></b-icon>
          <b-icon stacked icon="chevron-right"></b-icon>
        </b-iconstack>
      </div>
      <div class="face">
        <img
          class="face__part face__base"
          :src="require(`../assets/faces/${characters[base]}/base.png`)"
        />
        <img
          class="face__part face__augu"
          :src="require(`../assets/faces/${characters[augu]}/augu.png`)"
        />
        <img
          class="face__part face__munnur"
          :src="require(`../assets/faces/${characters[munnur]}/munnur.png`)"
        />
      </div>
      <div class="character__selection">
        <b-iconstack
          font-scale="1.75"
          class="pagination__arrow"
          @click="next('base')"
        >
          <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
          <b-icon stacked icon="circle"></b-icon>
          <b-icon stacked icon="chevron-right"></b-icon>
        </b-iconstack>
        <b-iconstack
          font-scale="1.75"
          class="pagination__arrow"
          @click="next('augu')"
        >
          <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
          <b-icon stacked icon="circle"></b-icon>
          <b-icon stacked icon="chevron-right"></b-icon>
        </b-iconstack>
        <b-iconstack
          font-scale="1.75"
          class="pagination__arrow"
          @click="next('munnur')"
        >
          <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
          <b-icon stacked icon="circle"></b-icon>
          <b-icon stacked icon="chevron-right"></b-icon>
        </b-iconstack>
      </div>
    </b-row>
    <span class="character__name">{{ name }}</span>
  </b-container>
</template>

<script>
import { capitalizeFirstLetter } from "../utils/helpers";
export default {
  name: "CharacterCreation",
  components: {},

  data() {
    const chars = [
      "Ægir",
      "Bjartur",
      "Ásgrímur",
      "Einar",
      "Eyvindur",
      "Finnbogi",
      "Helgi",
      "Hjálmar",
      "Jóhannes",
      "Arnaldur",
    ];
    const start = Math.floor(Math.random() * chars.length);
    return {
      characters: chars.sort(() => 0.5 - Math.random()),
      munnur: start,
      base: start,
      augu: start,
    };
  },

  computed: {
    name() {
      if (
        this.characters[this.augu].length === 4 &&
        this.characters[this.base].length === 4 &&
        this.characters[this.munnur].length === 4
      ) {
        return this.characters[this.augu];
      }
      const first = this.splitString(this.characters[this.base]);
      const middle = this.splitString(this.characters[this.augu]);
      const last = this.splitString(this.characters[this.munnur]);
      const name = first[0] + middle[1] + last[last.length - 1];
      return capitalizeFirstLetter(name);
    },
  },

  methods: {
    next(type) {
      this[type] = (this[type] + 1) % this.characters.length;
    },
    prev(type) {
      if (this[type] === 0) {
        this[type] = this.characters.length - 1;
      } else {
        this[type] -= 1;
      }
    },
    splitString(string) {
      const regex = RegExp(".{1," + Math.ceil(string.length / 3) + "}", "g");
      return string.match(regex);
    },
  },
};
</script>

<style lang="scss">
@import "~@/assets/scss/vendors/bootstrap-vue/index";
.character-creation {
  &__container {
    height: 550px;
    min-width: 90%;
  }
}

.character {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  position: relative;
  height: 90%;

  &__name {
    display: flex;
    justify-content: center;
    font-size: 30px;
  }

  &__selection {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
    svg {
      margin-bottom: 100px;
    }
  }
}

.face {
  &__part {
    position: absolute;
    left: 0;
    right: 0;
    margin-left: auto;
    margin-right: auto;
    width: 400px;
    height: 500px;
    @include media-breakpoint-down(sm) {
      & {
        width: 250px;
        height: 400px;
      }
    }
  }
  &__munnur {
    top: 10px;
  }
  &__augu {
    z-index: 10;
  }
}
</style>
