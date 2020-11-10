// https://medium.com/javascript-in-plain-english/state-management-with-react-hooks-no-redux-or-context-api-8b3035ceecf8
import React from 'react'
import useGlobalHook from '../hooks/useGlobalHook'
import * as actions from './actions'

const initialState = { canvas: { bgURL: '' } }

const useGlobal = useGlobalHook(React, initialState, actions)

export default useGlobal
