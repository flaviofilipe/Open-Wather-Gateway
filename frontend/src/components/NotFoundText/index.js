import React from 'react'
import {Message} from './styles'

const NotFoundText = ({show}) => {
    return (
        <Message show={show}>Sorry. We couldn't find the specified city.</Message>
    );
}

export default NotFoundText;