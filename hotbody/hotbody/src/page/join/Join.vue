<template>
  <div class="slide">
    <div class="slide_sub list">
      <div class="sub_txt">
        건강 관리를 위해<br class="nl" />
        회원님의 정보와 목표,<br class="nl" />
        생활습관을 알려주세요.
      </div>
      <div class="sub_imgs">
        <template v-if="page == 1">
          <div>
            <img class="sub_img" src="../../assets/imgs/join1.jpg" />
          </div>
        </template>
        <template v-if="page == 2">
          <div>
            <img class="sub_img" src="../../assets/imgs/join2.jpg" />
          </div>
        </template>
        <template v-if="page == 3">
          <div>
            <img class="sub_img" src="../../assets/imgs/join3.jpg" />
          </div>
        </template>
        <template v-if="page == 4">
          <div>
            <img class="sub_img" style="margin:27vh 0 0 9vw; width: 10vw;" src="../../assets/imgs/join6.jpg" />
          </div>
        </template>
        <template v-if="page == 5">
          <div>
            <img class="sub_img" src="../../assets/imgs/join5.jpg" />
          </div>
        </template>
      </div>
    </div>

    <div class="slide_main list">
      <template v-if="page == 1">
        <div class="content_">
          <!-- <div class="conten_1"> -->
          <div class="headarea">
            <input
              v-model="nickname"
              id="nickname"
              type="text"
              @keyup.enter="login"
              placeholder="닉네임을 입력해주세요"
            />
          </div>

          <div class="check">{{ nickcheck }}</div>

          <br />
          <div class="main_question">나이가 어떻게 되시나요?</div>
          <div class="subjective">
            <input
              class="sub_answer"
              v-model="age"
              id="age"
              type="text"
              maxlength="3"
            />
            <span class="sub_answer_unit">세</span>
          </div>
          <div class="check">{{ agecheck }}</div>
        </div>
      </template>
      <template v-else-if="page == 2">
        <div class="content_">
          <div class="main_question">현재 키와 몸무게가 어떻게 되시나요?</div>
          <div class="subjective">
            <input
              class="sub_answer"
              v-model="height"
              id="height"
              type="text"
              maxlength="5"
            />
            <span class="sub_answer_unit">cm</span>
            <div class="check">{{ heicheck }}</div>
            <input
              class="sub_answer"
              v-model="weight"
              id="weight"
              type="text"
              maxlength="5"
            />
            <span class="sub_answer_unit">kg</span>
            <div class="check">{{ weicheck }}</div>
          </div>
        </div>
      </template>
      <template v-else-if="page == 3">
        <div class="content_">
          <div class="main_question">성별이 무엇인가요?</div>
          <div class="gen">
            <div class="imgs flexs">
              <div>
                <img
                  class="img_gen"
                  @click="inputgender(1)"
                  src="../../assets/imgs/woman.png"
                />
              </div>
              <div>
                <img
                  class="img_gen"
                  @click="inputgender(2)"
                  src="../../assets/imgs/man.png"
                />
              </div>
            </div>
            <div class="flexs radios radios2">
              <input
                type="radio"
                name="radio1"
                id="woman"
                value="1"
                v-model="gender"
              />
              <label class="four col" for="woman">여성</label>
              <input
                type="radio"
                name="radio1"
                id="man"
                value="2"
                v-model="gender"
              />
              <label class="four col" for="man">남성</label>
            </div>
          </div>
        </div>
      </template>
      <template v-else-if="page == 4">
        <div class="content_">
          <div class="main_question">얼마나 활동적이세요?</div>
          <div class="radios radios1">
            <input
              type="radio"
              name="radio1"
              id="very"
              value="1"
              v-model="activity"
            />
            <label class="four col" for="very">매우 활동적</label>
            <input
              type="radio"
              name="radio1"
              id="nomal"
              value="2"
              v-model="activity"
            />
            <label class="four col" for="nomal">활동적</label>
            <input
              type="radio"
              name="radio1"
              id="small"
              value="3"
              v-model="activity"
            />
            <label class="four col" for="small">저 활동적</label>
            <input
              type="radio"
              name="radio1"
              id="nomove"
              value="4"
              v-model="activity"
            />
            <label class="four col" for="nomove">비 활동적</label>
          </div>
        </div>
      </template>
      <template v-else-if="page == 5">
        <div class="content_">
          <div class="main_question">목표가 있으신가요?</div>
          <div class="radios radios1">
            <input
              type="radio"
              name="radio1"
              id="short"
              value="1"
              v-model="goal"
            />
            <label class="four col" for="short">체중 감소</label>
            <input
              type="radio"
              name="radio1"
              id="keep"
              value="2"
              v-model="goal"
            />
            <label class="four col" for="keep">체중 유지</label>
            <input
              type="radio"
              name="radio1"
              id="long"
              value="3"
              v-model="goal"
            />
            <label class="four col" for="long">체중 증가</label>
          </div>
        </div>
      </template>
      <div class="showpage">
        <div>{{ page }}/5</div>
      </div>
      <div class="flexs btnSetss">
        <template v-if="page != 1">
          <div class="btnJoin" @click="prePage()">이전</div>
        </template>
        <template v-else-if="page == 1">
          <div class="margin1" />
        </template>
        <template v-if="page == 5">
          <div class="btnJoin" @click="checkHandler">설정완료</div>
        </template>
        <template v-else-if="page != 5">
          <div class="btnJoin" @click="movePage()">다음</div>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      page: 1,
      nickname: "",
      age: "",
      height: "",
      weight: "",
      gender: 0,
      activity: 0,
      goal: 0,
      nickcheck: "닉네임을 입력해주세요",
      agecheck: "나이를 입력해주세요",
      heicheck: "키는 80이상 입력해주세요",
      weicheck: "몸무게는 30이상을 입력해주세요",
      alertDialog1Visible: false,
      // items: [],
    };
  },
  watch: {
    age: function () {
      this.agefail(this.age);
    },
    nickname: function () {
      this.nickfail(this.nickname);
    },
    height: function () {
      this.heightfail(this.height);
    },
    weight: function () {
      this.weightfail(this.weight);
    },
  },
  created() {
    this.$store.commit("getpk");
  },
  methods: {
    movePage() {
      if (this.page == 1 && (this.nickname == "" || this.agecheck != "")) {
        alert("닉네임과 나이를 입력해주세요.");
      } else if (
        this.page == 2 &&
        (this.weicheck != "" || this.heicheck != "")
      ) {
        alert("키와 몸무게를 입력해주세요.");
      } else if (this.page == 3 && this.gender == 0) {
        alert("성별이 선택되지 않았습니다.");
      } else if (this.page == 4 && this.activity == 0) {
        alert("평소 활동량을 체크해주세요");
      } else {
        this.page++;
      }
    },
    checkHandler() {
      if (this.page == 5 && this.goal == 0) {
        alert("목표를 체크해주세요");
      } else {
        // console.log(
        //   "join page - 저장된 userpk :" + localStorage.getItem("userpk")
        // );
        this.createHandler();
      }
    },
    prePage() {
      this.page--;
    },
    Join() {},
    inputgender(index) {
      this.gender = index;
      // console.log(this.gender);
    },
    nickfail: function (text) {
      if (text.length < 1) {
        this.nickcheck = "닉네임을 입력해주세요.";
      } else {
        this.nickcheck = "";
      }
    },
    agefail: function (text) {
      if (text[0] == "0") {
        text = text.substring(1, 5);
        this.age = text;
      }
      var len = text.length;
      if (text[len - 1] < "0" || text[len - 1] > "9") {
        text = text.substring(0, len - 1);
        this.age = text;
      }

      var tmp = Number(text);
      if (tmp <= 0 || isNaN(tmp)) {
        this.agecheck = "나이를 입력해주세요.";
      } else {
        this.agecheck = "";
      }
      if (isNaN(tmp)) {
        this.age = "";
      } else {
        this.age = String(tmp);
      }
    },
    heightfail: function (text) {
      var spn;
      if (text[0] == "0") {
        text = text.substring(1, 5);
        this.height = text;
      }

      var len = text.length;
      if (
        (text[len - 1] < "0" || text[len - 1] > "9") &&
        text[len - 1] != "."
      ) {
        text = text.substring(0, len - 1);
        this.age = text;
      }

      var tmp = Number(text);
      if (text.indexOf(".") == -1 && (isNaN(tmp) || tmp < 1)) {
        this.height = String("");
      }
      if (text.indexOf(".") == -1) {
        spn = text.length;
        if (spn > 3) {
          this.heicheck = "키가 3자리를 넘습니다. 다시확인해주세요.";
        } else if (spn == 3) {
          this.heicheck = "";
        } else if (spn == 2) {
          if (tmp < 80) {
            this.heicheck = "키는 80을 넘어야 합니다.";
          } else {
            this.heicheck = "";
          }
        } else {
          this.heicheck = "키는 80을 넘어야 합니다.";
        }
      } else {
        var sp = text.split(".");
        spn = sp.length - 1;

        if (sp[0].length > 3) {
          this.heicheck = "키가 3자리를 넘습니다. 다시확인해주세요.";
        } else if (sp[0].length == 3) {
          this.heicheck = "";
        } else if (sp[1].length > 1) {
          this.heicheck = "소수점은 한자리만 입력해주세요.";
        } else if (spn > 1) {
          this.heicheck = "콤마가 1개가 넘습니다!!";
        } else {
          if (tmp <= 80) {
            this.heicheck = "키가 잘못 입력된거 같습니다...";
          } else if (isNaN(tmp)) {
            this.heicheck = "키를 입력해주세요.";
          } else {
            this.heicheck = "";
          }
        }
      }
    },
    weightfail: function (text) {
      var spn;
      if (text[0] == "0") {
        text = text.substring(1, 5);
        this.weight = text;
      }
      var tmp = Number(text);
      if (isNaN(tmp) || tmp < 1) {
        this.weight = String("");
      }
      if (text.indexOf(".") == -1) {
        spn = text.length;
        if (spn > 3) {
          this.weicheck = "몸무게가 3자리를 넘습니다. 다시확인해주세요.";
        } else if (spn == 3) {
          this.weicheck = "";
        } else if (spn == 2) {
          if (tmp < 30) {
            this.weicheck = "몸무게는 30을 넘어야 합니다.";
          } else {
            this.weicheck = "";
          }
        } else {
          this.weicheck = " 몸무게는 30을 넘어야 합니다.";
        }
      } else {
        var sp = text.split(".");
        spn = sp.length - 1;

        if (sp[0].length > 3) {
          this.weicheck = "몸무게가 3자리를 넘습니다. 다시확인해주세요.";
        } else if (sp[0].length == 3) {
          this.weicheck = "";
        } else if (sp[1].length > 1) {
          this.weicheck = "소수점은 한자리만 입력해주세요.";
        } else if (spn > 1) {
          this.weicheck = "콤마가 1개가 넘습니다!!";
        } else {
          if (tmp <= 30) {
            this.weicheck = "몸무게가 잘못 입력된거 같습니다.";
          } else if (isNaN(tmp)) {
            this.weicheck = "몸무게를 입력해주세요";
          } else {
            this.weicheck = "";
          }
        }
      }
    },

    createHandler() {
      axios
        .post(
          `http://127.0.0.1:8000/accounts/initinfo/${localStorage.getItem(
            "userpk"
          )}/`,
          {
            nickname: this.nickname,
            age: this.age,
            height: this.height,
            weight: this.weight,
            gender: this.gender,
            activity: this.activity,
            goal: this.goal,
          }
        )
        .then(({ data }) => {
          if (data) {
            // console.log(data);
            this.$store.commit("Savenickname", this.nickname);
            this.$store.state.usergoal = this.goal;
            this.$store.state.loadingflag = true;
          } else {
            alert("등록 중 오류발생!");
          }
        })
        .catch((error) => {
          this.error = error;
        })
        .finally(() => {
          this.$router.push("/main");
        });
    },
  },
};
</script>

<style scoped>
@import "../../assets/css/join.css";
</style>
