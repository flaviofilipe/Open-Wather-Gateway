import styled from 'styled-components'

export const Message = styled.h1`
  text-align: center;
  color: red;
  display: ${prpos => prpos.show ? 'block' : 'none'};
`;
