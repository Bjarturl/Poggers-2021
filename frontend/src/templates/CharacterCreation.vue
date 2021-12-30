<template>
  <Loading v-if="fetching" />
  <b-container class="character-creation__container" v-else-if="!fighting">
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
      <div class="w-100 d-flex justify-content-between pt-5">
        <button
          class="character__button character__button--random"
          @click="randomize"
        >
          Random
        </button>
        <h1 class="text-center">{{ name }}</h1>
        <button class="character__button" @click="startFight">BERJAST!!</button>
      </div>
    </b-row>
  </b-container>
  <!-- FIGHTING -->
  <b-container
    v-else
    class="fight-container"
    @click="$root.$emit('bv::hide::tooltip')"
  >
    <div class="fighter__container">
      <div class="fighter">
        <div class="fighter__face">
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
        </div>
        <div class="d-flex justify-content-start">
          <b-progress
            :max="stats.HP"
            :value="HP < 0 ? 0 : HP"
            height="2rem"
            class="w-75 text-center"
            variant="success"
            animated
            show-value
          >
          </b-progress>
        </div>
        <div class="fighter__stats">
          <span class="fighter__stats--name">{{ name }}</span>
          <span>ATK: {{ stats.ATK }}</span>
          <span>DEF: {{ stats.DEF }}%</span>
          <span>MAX HP: {{ stats.HP }}</span>
          <span>CRIT: {{ stats.CRIT }}%</span>
          <span>ACC: {{ stats.ACC }}%</span>
          <button
            class="character__button character__button--random mt-4"
            v-if="!attacking && !finished"
            @click="attack"
          >
            ÁRÁS
          </button>
        </div>
      </div>
      <div>
        <img class="vs" :src="require(`../assets/vs.png`)" />
      </div>
      <div class="fighter fighter__computer">
        <div class="fighter__face">
          <div class="face">
            <img
              class="face__part face__base"
              :src="
                require(`../assets/faces/${characters[opponentBase]}/base.png`)
              "
            />
            <img
              class="face__part face__augu"
              :src="
                require(`../assets/faces/${characters[opponentAugu]}/augu.png`)
              "
            />
            <img
              class="face__part face__munnur"
              :src="
                require(`../assets/faces/${characters[opponentMunnur]}/munnur.png`)
              "
            />
          </div>
        </div>
        <div class="d-flex justify-content-end">
          <b-progress
            :max="opponentStats.HP"
            :value="opponentHP < 0 ? 0 : opponentHP"
            height="2rem"
            class="w-75 text-center front"
            variant="success"
            animated
            show-value
          >
          </b-progress>
        </div>
        <div class="fighter__stats">
          <span class="fighter__stats--name">{{ opponentName }} (AI)</span>
          <span>ATK: {{ opponentStats.ATK }}</span>
          <span>DEF: {{ opponentStats.DEF }}%</span>
          <span>MAX HP: {{ opponentStats.HP }}</span>
          <span>CRIT: {{ opponentStats.CRIT }}%</span>
          <span>ACC: {{ opponentStats.ACC }}%</span>
        </div>
      </div>
    </div>
    <div class="w-100 d-flex justify-content-between footer-container">
      <button
        class="character__button--stop w-25"
        :disabled="attacking"
        @click="stopFight"
      >
        <b-icon icon="arrow-left" style="width: 15px; height: 15px"></b-icon>
        Hætta
      </button>
      <div class="footer-container__combat w-100">
        <span>{{ combatText }}</span>
      </div>
      <div class="w-50 text-left">
        <span class="font-italic"
          >Stats
          <span class="ml-1">
            <b-icon
              id="question-tooltip"
              icon="question-circle"
              style="width: 15px; height: 15px"
            ></b-icon>
            <b-tooltip
              target="question-tooltip"
              triggers="hover click"
              placement="topleft"
            >
              <div class="tooltip__tip d-flex flex-column">
                <span><strong>ATK: </strong>Fjöldi sendra skilaboða</span>
                <span><strong>DEF: </strong> Fjöldi sendra mynda</span>
                <span><strong>MAX HP: </strong> Fjöldi reactions fengin</span>
                <span
                  ><strong>CRIT: </strong> Fjöldi reactions sem manneskja gaf
                  (fleiri = minna crit)</span
                >
                <span
                  ><strong>ACC: </strong>Lengsta skilaboð sent (styttra = betra
                  accuracy)
                </span>

                <span class="mt-2"
                  >ATH. stats breytast eftir því hvaða ár er valið</span
                >
              </div>
            </b-tooltip>
          </span>
        </span>
      </div>
    </div>
  </b-container>
</template>

<script>
import { capitalizeFirstLetter } from "../utils/helpers";
import { GET } from "../data/api";
import Loading from "../components/Loading.vue";
export default {
  name: "CharacterCreation",
  components: {
    Loading,
  },

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
      "Ingvar",
      "Jón Egill",
      "Kristófer",
      "Manfreð",
      "Sindri",
    ];
    const start = Math.floor(Math.random() * chars.length);
    return {
      characters: chars.sort(() => 0.5 - Math.random()),
      munnur: start,
      base: start,
      augu: start,
      stats: {},
      opponentStats: {},
      fighting: false,
      opponentBase: 0,
      opponentAugu: 0,
      opponentMunnur: 0,
      fetching: false,
      combatText: "",
      attacking: false,
      finished: false,
      HP: 0,
      opponentHP: 0,
    };
  },

  computed: {
    name() {
      return this.getName(this.augu, this.base, this.munnur);
    },
    opponentName() {
      return this.getName(
        this.opponentAugu,
        this.opponentBase,
        this.opponentMunnur
      );
    },
  },

  methods: {
    next(type) {
      this[type] = (this[type] + 1) % this.characters.length;
    },
    stopFight() {
      this.fighting = false;
      this.$emit("toggling", false);
    },
    async fetchData() {
      this.fetching = true;
      this.stats = {
        ATK: 0,
        DEF: 0,
        ACC: 0,
        CRIT: 0,
        HP: 0,
      };
      this.opponentStats = Object.assign({}, this.stats);
      await GET.battleStats(this.$store.year).then(
        function (data) {
          const statsArray = data[0]["battle_stats"];
          let user = [
            this.characters[this.augu],
            this.characters[this.base],
            this.characters[this.munnur],
          ];
          let computer = [
            this.characters[this.opponentAugu],
            this.characters[this.opponentBase],
            this.characters[this.opponentMunnur],
          ];
          for (let u of user) {
            let userStats = statsArray.find(
              (s) => s.Name.split(" ")[0] === u.split(" ")[0]
            );
            this.stats.ATK += userStats.ATK;
            this.stats.DEF += userStats.DEF;
            this.stats.ACC += userStats.ACC;
            this.stats.CRIT += userStats.CRIT;
            this.stats.HP += userStats.HP;
          }
          this.stats.ATK = (this.stats.ATK / 3).toFixed(0);
          this.stats.DEF = ((this.stats.DEF / 3) * 100).toFixed(2);
          this.stats.ACC = ((this.stats.ACC / 3) * 100).toFixed(2);
          this.stats.CRIT = ((this.stats.CRIT / 3) * 100).toFixed(2);
          this.stats.HP = (this.stats.HP / 3).toFixed(0);
          for (let u of computer) {
            let opponentStats = statsArray.find(
              (s) => s.Name.split(" ")[0] === u.split(" ")[0]
            );
            this.opponentStats.ATK += opponentStats.ATK;
            this.opponentStats.DEF += opponentStats.DEF;
            this.opponentStats.ACC += opponentStats.ACC;
            this.opponentStats.CRIT += opponentStats.CRIT;
            this.opponentStats.HP += opponentStats.HP;
          }
          this.opponentStats.ATK = (this.opponentStats.ATK / 3).toFixed(0);
          this.opponentStats.DEF = ((this.opponentStats.DEF / 3) * 100).toFixed(
            2
          );
          this.opponentStats.ACC = ((this.opponentStats.ACC / 3) * 100).toFixed(
            2
          );
          this.opponentStats.CRIT = (
            (this.opponentStats.CRIT / 3) *
            100
          ).toFixed(2);
          this.opponentStats.HP = (this.opponentStats.HP / 3).toFixed(0);
        }.bind(this)
      );
      this.fetching = false;
      this.HP = this.stats.HP;
      this.opponentHP = this.opponentStats.HP;
      this.combatText = `It's ${this.name}'s turn.`;
    },
    prev(type) {
      if (this[type] === 0) {
        this[type] = this.characters.length - 1;
      } else {
        this[type] -= 1;
      }
    },
    async sleep(time = 2000) {
      return await new Promise((r) => setTimeout(r, time));
    },

    async writeCombatText() {
      await new Promise((r) => {
        let str = this.combatText;
        let index = 0;
        this.combatText = "";
        let interval = setInterval(() => {
          if (this.combatText.length < str.length) {
            this.combatText = str.substring(0, index);
            index += 1;
          } else {
            clearInterval(interval);
            return setTimeout(r, 1000);
          }
        }, 50);
      });
    },

    async attack() {
      this.attacking = true;
      await this.performAttack().then(() => {
        this.sleep().then(() => {
          this.attacking = false;
          if (!this.finished) {
            this.combatText = `It's ${this.name}'s turn.`;
          }
        });
      });
    },
    async performAttack() {
      const attacks = [
        "bites",
        "shanks",
        "licks",
        "kicks",
        "punches",
        "headbutts",
        "pinches",
        "vomits on",
      ];

      let places = [
        "head",
        "tooth",
        "face",
        "leg",
        "arm",
        "ass",
        "ear",
        "pener",
        "eyes",
        "chin",
        "shin",
      ];
      this.combatText = `${this.name} ${
        attacks[Math.floor(Math.random() * attacks.length)]
      } ${this.opponentName} in the ${
        places[Math.floor(Math.random() * places.length)]
      }...`;
      await this.writeCombatText();
      let acc = Math.random();
      let def = Math.random();
      let crit = Math.random();
      if (acc > this.stats.ACC / 100) {
        this.combatText = `${this.name} misses his attack. Vandró...`;
      } else if (def <= this.opponentStats.DEF / 100) {
        this.combatText = `${this.opponentName} blocks the attack from ${this.name}. Tekinn lúser...`;
      } else if (crit <= this.opponentStats.CRIT / 100) {
        this.combatText = `${this.name} attacks ${
          this.opponentName
        } WITH A CRITICAL HIT, dealing ${this.stats.ATK * 2} points of damage.`;
        this.opponentHP -= this.stats.ATK * 2;
      } else {
        this.combatText = `${this.name} delivers a devastating blow to ${this.opponentName}, inflicting ${this.stats.ATK} points of damage.`;
        this.opponentHP -= this.stats.ATK;
      }
      await this.writeCombatText();

      if (this.opponentHP <= 0) {
        this.finished = true;
        this.combatText = `${this.name} has defeated ${this.opponentName} in glorious combat!!`;
        await this.writeCombatText();
        return;
      }
      this.combatText = `It's ${this.opponentName} (AI)'s turn.`;
      await this.writeCombatText();

      this.combatText = `${this.opponentName} ${
        attacks[Math.floor(Math.random() * attacks.length)]
      } ${this.name} in the ${
        places[Math.floor(Math.random() * places.length)]
      }...`;
      await this.writeCombatText();
      acc = Math.random();
      def = Math.random();
      crit = Math.random();
      if (acc > this.opponentStats.ACC / 100) {
        this.combatText = `${this.opponentName} misses his attack. Vandró...`;
        await this.writeCombatText();
        return;
      }
      if (def <= this.stats.DEF / 100) {
        this.combatText = `${this.name} blocks the attack from ${this.opponentName}. Tekinn lúser...`;
        await this.writeCombatText();
        return;
      }
      if (crit <= this.stats.CRIT / 100) {
        this.combatText = `${this.opponentName} attacks ${
          this.name
        } WITH A CRITICAL HIT, dealing ${
          this.opponentStats.ATK * 2
        } points of damage.`;
        this.HP -= this.opponentStats.ATK * 2;
      } else {
        this.combatText = `${this.opponentName} delivers a devastating blow to ${this.name}, inflicting ${this.opponentStats.ATK} points of damage.`;
        this.HP -= this.opponentStats.ATK;
      }
      await this.writeCombatText();
      if (this.HP <= 0) {
        this.finished = true;
        this.combatText = `${this.opponentName} has defeated ${this.name} in glorious combat!!`;
        await this.writeCombatText();
        return;
      }
    },
    getName(augu, base, munnur) {
      if (
        this.characters[augu].length === 4 &&
        this.characters[base].length === 4 &&
        this.characters[munnur].length === 4
      ) {
        return this.characters[augu];
      }
      const first = this.splitString(this.characters[base]);
      const middle = this.splitString(this.characters[augu]);
      const last = this.splitString(this.characters[munnur]);
      const name = first[0] + middle[1] + last[last.length - 1];
      return capitalizeFirstLetter(name);
    },
    async startFight() {
      this.fighting = true;
      this.finished = false;
      this.opponentBase = Math.floor(Math.random() * this.characters.length);
      this.opponentAugu = Math.floor(Math.random() * this.characters.length);
      this.opponentMunnur = Math.floor(Math.random() * this.characters.length);
      this.$emit("toggling", true);
      await this.fetchData();
    },
    splitString(string) {
      const regex = RegExp(".{1," + Math.ceil(string.length / 3) + "}", "g");
      return string.match(regex);
    },
    randomize() {
      this.base = Math.floor(Math.random() * this.characters.length);
      this.augu = Math.floor(Math.random() * this.characters.length);
      this.munnur = Math.floor(Math.random() * this.characters.length);
    },
  },
};
</script>

<style lang="scss">
@import "~@/assets/scss/vendors/bootstrap-vue/index";
@include media-breakpoint-down(sm) {
  .main-container {
    height: 95vh !important;
  }
}

.footer-container {
  padding-bottom: 80px;
  &__combat {
    width: 70%;
    margin-top: -70px;
    @include media-breakpoint-down(sm) {
      & {
        width: 100%;
        margin-left: 0;
      }
    }
    margin-left: 100px;
    text-align: center;
    font-size: 20px;
  }
}

.character-creation {
  &__container {
    padding-top: 40px;
    height: 550px;
    min-width: 90%;
    padding-bottom: 40px;
  }
}

.fight-container {
  height: 100%;
  min-width: 90%;
  font-family: "Fredoka one";
  font-size: 16px;
}

.tooltip {
  &__tip {
    background: #f79824;
    z-index: 10;
    padding: 10px;
    width: 75%;
    margin-left: -120px;
    margin-top: -20px;
    font-style: normal;
  }
  @include media-breakpoint-down(sm) {
    & {
      width: 50%;
    }
  }
}

.vs {
  height: 100px;
  width: 150px;
  margin-top: 60px;
  @include media-breakpoint-down(sm) {
    & {
      width: 100px;
      height: 100px;
      margin-left: 20px;
    }
  }
}

.fighter {
  width: 50%;
  height: 75%;
  @include media-breakpoint-down(sm) {
    & {
      width: 100%;
    }
  }
  position: relative;
  &__container {
    display: flex;
    justify-content: space-around;
    position: relative;
    height: 90%;
    width: 100%;
  }
  &__face {
    display: flex;
    flex-direction: column;
  }

  &__stats {
    display: flex;
    flex-direction: column;
    font-weight: bold;
    &--name {
      font-weight: normal;
      font-size: 20px;
    }
    position: absolute;
    left: 70px;
    @include media-breakpoint-down(sm) {
      & {
        left: 10px;
        width: 100%;
      }
    }
    right: auto;
  }
  .face {
    height: 250px;
    &__part {
      width: 200px;
      height: 250px;
      left: 0;
      right: auto;
      top: 5px;
      @include media-breakpoint-down(sm) {
        & {
          width: 150px;
          height: 200px;
          left: -30px;
        }
      }
    }
  }
  &__computer {
    .fighter__stats {
      position: absolute;
      left: auto;
      right: 70px;
      @include media-breakpoint-down(sm) {
        & {
          right: 10px;
        }
      }
    }
    .face {
      &__part {
        left: auto;
        right: 0;
        @include media-breakpoint-down(sm) {
          & {
            right: -50px;
          }
        }
      }
    }
  }
}

.character {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  position: relative;
  height: 90%;
  margin-top: -30px;

  &__button {
    background-color: rgba(#00ff00, 0.7);
    font-weight: bold;
    color: white;
    border: none;
    border-radius: 20px;
    padding: 15px;
    &--random {
      background-color: rgba(#ff0000, 0.6);
    }
    &--stop {
      background-color: #242424;
      color: white;
      font-size: 18px;
      border-radius: 35px;
      border: none;
      @include media-breakpoint-down(sm) {
        & {
          display: flex;
          justify-content: center;
          align-items: center;
          height: 40px;
          padding: 10px;
        }
      }
    }
  }

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
    padding: 8px;
    svg {
      fill: #242424;
      stroke: white;
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
