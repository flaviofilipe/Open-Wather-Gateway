import React from 'react'
import { Card, CardDescriptions, CardTemp} from './styles'

const CityWeatherCard = ({data, show=true}) => {
    return (
        <Card show={show}>
            <CardDescriptions>{data.city}</CardDescriptions>
            <CardTemp>{data.temperature}</CardTemp>
            <CardDescriptions>{data.description}</CardDescriptions>
        </Card>
    )
}

export default CityWeatherCard;