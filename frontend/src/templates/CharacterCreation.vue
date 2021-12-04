<template>
  <b-container class="character-creation__container">
    <div class="character">
      <div class="character__selection">
        <b-iconstack
          rotate="180"
          font-scale="1.75"
          class="pagination__arrow"
          @click="prev('hair')"
        >
          <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
          <b-icon stacked icon="circle"></b-icon>
          <b-icon stacked icon="chevron-right"></b-icon>
        </b-iconstack>
        <b-iconstack
          rotate="180"
          font-scale="1.75"
          class="pagination__arrow"
          @click="prev('upper')"
        >
          <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
          <b-icon stacked icon="circle"></b-icon>
          <b-icon stacked icon="chevron-right"></b-icon>
        </b-iconstack>
        <b-iconstack
          rotate="180"
          font-scale="1.75"
          class="pagination__arrow"
          @click="prev('lower')"
        >
          <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
          <b-icon stacked icon="circle"></b-icon>
          <b-icon stacked icon="chevron-right"></b-icon>
        </b-iconstack>
      </div>
      <div class="face">
        <img
          class="face__part face__hair"
          :src="require(`../assets/faces/hair/${characters[hair]}.png`)"
        />
        <img
          class="face__part face__upper"
          :src="require(`../assets/faces/upper/${characters[upper]}.png`)"
        />
        <img
          class="face__part face__lower"
          :src="require(`../assets/faces/lower/${characters[lower]}.png`)"
        />
      </div>
      <div class="character__selection">
        <b-iconstack
          font-scale="1.75"
          class="pagination__arrow"
          @click="next('hair')"
        >
          <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
          <b-icon stacked icon="circle"></b-icon>
          <b-icon stacked icon="chevron-right"></b-icon>
        </b-iconstack>
        <b-iconstack
          font-scale="1.75"
          class="pagination__arrow"
          @click="next('upper')"
        >
          <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
          <b-icon stacked icon="circle"></b-icon>
          <b-icon stacked icon="chevron-right"></b-icon>
        </b-iconstack>
        <b-iconstack
          font-scale="1.75"
          class="pagination__arrow"
          @click="next('lower')"
        >
          <b-icon stacked icon="circle-fill" variant="secondary"></b-icon>
          <b-icon stacked icon="circle"></b-icon>
          <b-icon stacked icon="chevron-right"></b-icon>
        </b-iconstack>
      </div>
    </div>
    <span class="character__name">{{ name }}</span>
  </b-container>
</template>

<script>
import { capitalizeFirstLetter } from "../utils/helpers";
export default {
  name: "CharacterCreation",
  components: {},

  data() {
    return {
      characters: ["eyvindur", "ingvar"],
      hair: 0,
      upper: 0,
      lower: 0,
    };
  },

  computed: {
    name() {
      const first = this.splitString(this.characters[this.hair]);
      const middle = this.splitString(this.characters[this.upper]);
      const last = this.splitString(this.characters[this.lower]);
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
    min-width: 100%;
  }
}

.character {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  position: relative;
  height: 100%;

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
  }
  &__hair {
    top: 10px;
  }
  &__lower {
    z-index: 10;
  }
}
</style>
