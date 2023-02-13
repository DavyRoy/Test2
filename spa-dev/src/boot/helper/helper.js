export function getPercent(startedDate, endedDate) {
  return ((Date.now().valueOf() - new Date(startedDate).valueOf()) / (new Date(endedDate).valueOf() - new Date(startedDate).valueOf()))
}

export function cutLongText(text, length) {
	if (text.length > length) {
		return text.slice(0, length) + '...'
	}
	return text
}
