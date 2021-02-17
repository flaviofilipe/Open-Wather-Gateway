import React from 'react'
import { List } from './styles'
import CityWeatherCard from '../CityWeatherCard'

const DATA = {
    "city": "London",
    "description": "broken clouds",
    "temperature": "9ºC"
  }
const HistoricList = ({data}) => {
    return (
        <List>
            <CityWeatherCard data={DATA} />
            <CityWeatherCard data={DATA} />
            <CityWeatherCard data={DATA} />
            <CityWeatherCard data={DATA} />
            <CityWeatherCard data={DATA} />
        </List>
    )
}

export default HistoricList;