import React from 'react'
import { Card, CardDescriptions, CardTemp} from './style'

const CityWeatherCard = () => {
    return (
        <Card>
            <CardDescriptions>Florianópolis</CardDescriptions>
            <CardTemp>22ºC</CardTemp>
            <CardDescriptions>Light Rain</CardDescriptions>
        </Card>
    )
}

export default CityWeatherCard;