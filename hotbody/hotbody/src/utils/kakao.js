import store from '@/store/index.js';
import axios from 'axios';
import {
    saveEmailToCookie,
    saveTokenToCookie,
    saveUserpkToCookie,
    deleteCookie 
} from '@/utils/cookies'
let onSuccess = (data) => {
    // console.log(data);
    // console.log('kakao-login success');
    GetMe(data);
};
let onFailure = (data) => {
    data
    // console.log('kakao-login failure');
};



let GetMe = async (authObj) => {
    authObj

    window.Kakao.API.request({
        url: '/v2/user/me',
        success: async (res) => {
            const kakao_account = res.kakao_account;
            // console.log('아이듸!')
            // console.log(res);
            // console.log(kakao_account);
            const req_body = {
                id: res.id,
                name: kakao_account.profile.nickname,
                email: kakao_account.email,
                // token: res.access_token,
                // birthday: kakao_account.birthday,
                // kakaoAccessToken: authObj.access_token,
                profileIMG: kakao_account.profile.profile_image_url,
            };
            // social_login(req_body);
            // console.log(req_body)
            // alert('로그인 했어용....')
            axios.post('http://127.0.0.1:8000/accounts/checked/',
            { 
                username: req_body.email
            })
            .then(res => {
                res
                axios.post('http://127.0.0.1:8000/accounts/user/login/',{
                    username: req_body.email,
                    password: '1234qwer!'
                })
                .then(res => {
                    // console.log(res.data)
                    saveTokenToCookie(res.data.token)
                    saveUserpkToCookie(res.data.user.pk)
                    saveEmailToCookie(req_body.email)
                    // console.log(req_body.profileIMG)
                    if(!req_body.profileIMG){
                        localStorage.setItem('userImg','https://i.stack.imgur.com/l60Hf.png')
                    }
                    else localStorage.setItem('userImg',req_body.profileIMG)

                    // console.log('login 유저 pk :' + res.data.user.pk)
                    store.commit('Savepk', res.data.user.pk)
                    store.commit('Savetoken', res.data.token)
                    store.commit('loginCheck',0)
                })
                .catch(res => {
                    res
                    alert('로그인 할 수 없습니다!')
                })
           
            })
            .catch(res => {
                res
                axios.post('http://127.0.0.1:8000/accounts/signup/',{
                        username: req_body.email,
                        password1: '1234qwer!',
                        password2: '1234qwer!',
                })
                .then(res => {
                    // console.log(res + 'DB 저장')
                    saveTokenToCookie(res.data.token)
                    saveUserpkToCookie(res.data.user.pk)
                    saveEmailToCookie(req_body.email)

                    // console.log('join 유저 pk :' + res.data.user.pk)
                    store.commit('Savepk', res.data.user.pk)
                    store.commit('Savetoken', res.data.token)
                    store.commit('loginCheck',1)
                    // console.log(store.state)
                    
                })
                .catch(res => {
                    res
                    alert('가입 할 수 없습니다. 다시 시도 해 주세요.')
                })
            })
        },
        fail: (error) => {
            // LoginFailure();
            error
        },
    });
};

let Logout = () => {
    // console.log('kakao Logout');
    deleteCookie('nickname');
    deleteCookie('email');
    deleteCookie('token')
    // window.Kakao.Auth.logout(() => {
    //     console.log('dd')
    //     console.log(window.Kakao.Auth.getAccessToken())
    // });

    window.Kakao.API.request({
        url: '/v1/user/unlink',
        success: function(response) {
            response
            // console.log('kakao.api')
            // console.log('kakao.auth')
            store.commit('clearLogin');
            // console.log('로그아웃')
            // console.log(store.state)
        },
        fail: function(error) {
            // console.log('errrrrr')
            //  console.log(error);
            error
        },

    });


};

export { onSuccess,onFailure,GetMe,Logout}
