//http requests
import axios from 'axios';

import { GET_PLAYERS, DELETE_PLAYERS } from './types';

//GET PLAYERS
export const getPlayers = () => dispatch => {
    axios.get('/api/captains')
    .then(res => {
        dispatch({
            type: GET_PLAYERS,
            payload: res.data
        });
    }) 
    .catch(err => console.log(err));
}

//DELETE PLAYERS
export const deletePlayers = (id) => dispatch => {
    axios.delete(`/api/captains/${id}`)
    .then(res => {
        dispatch({
            type: DELETE_PLAYERS,
            payload: id
        });
    })
    .catch(err => console.log(err));
}