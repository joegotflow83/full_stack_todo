export const apiDomain = "http://localhost:8000/api/v1"

export const loginUrl = apiDomain + '/auth/login/'

export const userUrl = apiDomain + '/users/'

export const signupUrl = apiDomain + '/auth/signup/'

export const getHeaders = function () {
  const tokenData = JSON.parse(window.localStorage.getItem('authUser'))
  const headers = {
    'Authorization': 'Token ' + tokenData.token
  }
  return headers
}
