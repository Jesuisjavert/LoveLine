<template>
  <div>
    <v-parallax
      height="200"
      src="../../assets/images/hero1.jpg"
     >
          <v-row
            align="center"
            justify="center"
          >
            <v-col class="text-center" cols="12">
              <h2 class="display-1 font-weight-thin mb-4">Login</h2>
              <h4 class="subheading">Login & Signup</h4>
            </v-col>
          </v-row>
        </v-parallax>
    <v-form>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" sm="4">
          <br>
          <v-text-field 
            label="ID" 
            :rules="[rules.required, rules.min]" hide-details="auto"
            v-model="logindata.email"
          ></v-text-field><br><br>
          <v-text-field
              v-model="logindata.password"
              :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
              :rules="[rules.required, rules.min]"
              :type="show1 ? 'text' : 'password'"
              name="input-10-1"
              label="Password"
              hint="At least 8 characters"
              counter
              @click:append="show1 = !show1"
              /><br>
        </v-col>
      </v-row>
      <v-row justify="center">
        <!-- Login button -->
        <v-btn class="ma-2" outlined color="pink" @click="login(logindata)">Login</v-btn>
        <v-btn class="ma-2" outlined color="pink" @click="logout()">Logout</v-btn>
        <!-- signup modal -->
        <v-dialog v-model="dialog" persistent max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              class="ma-2" 
              color="pink"
              outlined
              v-bind="attrs"
              v-on="on"
            >
              Sign up
            </v-btn>
          </template>
          <v-card>
            <v-card-title class="pink lighten-4" color="pink">
              <span class="headline"> ◽ 회원가입 (Signup) 💟</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <!-- <v-col cols="12" sm="6" md="6">
                    <v-text-field label="성(First Name)" required></v-text-field>
                  </v-col> -->
                  <v-col cols="12" sm="6" md="6">
                    <v-text-field
                      label="이름(Last Name)"
                      v-model="signupdata.nickname"
                      persistent-hint
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field 
                      label="Email" 
                      v-model="signupdata.email"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field 
                      label="Password" 
                      type="password" 
                      v-model="signupdata.password1"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-text-field 
                      label="PasswordConfirm" 
                      type="password" 
                      v-model="signupdata.password2"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <!-- <v-select
                      :items="['0-17', '18-29', '30-54', '54+']"
                      label="Age*"
                      v-model="signupdata.age"
                      required
                    ></v-select> -->
                    <v-text-field 
                      label="Age" 
                      type="text" 
                      v-model="signupdata.age"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-autocomplete
                      :items="['Skiing', 'Ice hockey', 'Soccer', 'Basketball', 'Hockey', 'Reading', 'Writing', 'Coding', 'Basejump']"
                      label="Interests"
                      
                      multiple
                    ></v-autocomplete>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="pink" text @click="dialog = false">Close</v-btn>
              <v-btn color="pink" text @click="signup(),dialog = false">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!-- modal 끝 -->
      </v-row>
    </v-container>
  </v-form>
  </div>
  
</template>
<script>
import axios from 'axios'
import { mapActions, mapGetters } from 'vuex'
 export default {
   name : 'Login',
    data () {
      return {
        dialog: false,
        show1: false,
        logindata: {
          email: '',
          password: '',
        },
        signupdata: {
          email:'',
          nickname: '',
          password1: '',
          password2: '',
          age: '',
        },
        rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
          // emailMatch: () => ('The email and password you entered don\'t match'),
        },
      }
    },
    methods :{
      signup(){
        console.log('들어왔네요')
        axios.post('http://j3c202.p.ssafy.io:8000/api/rest-auth/signup/',this.signupdata)
        .then((res)=>{
          console.log(res)
        })
        .catch((err)=>{
          console.log(err.response)
        })
      },
      ...mapActions('accounts', ['login', 'logout'])
  
      // async login(){
      //   console.log('login 되었네요')
      //   const logindata = {
      //     email : this.email,
      //     password : this.password
      //   }
      //   const response = await axios.post('http://j3c202.p.ssafy.io:8000/api/rest-auth/login/',logindata)
      //   .catch((err)=>{
      //     console.log('에러페이지')
      //   })
      //   const headers = {
      //     Authorization : `Token ${response.data.key}`
      //   }
      //   console.log(headers,'-----')
      //   const userdata = await axios.get('http://j3c202.p.ssafy.io:8000/api/account',{headers :headers})
      //   .catch((err)=>{
      //     console.log(err.response)
      //   })
      //   console.log(userdata)
      // }

    }
  }
</script>

<style>

</style>