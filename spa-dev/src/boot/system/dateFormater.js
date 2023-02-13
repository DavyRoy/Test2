import { date } from 'quasar';

export function utcToDate(utc, splitterDate = '-', splitterTime = '-') {
  const sourceDate = new Date(utc);
  return {
    date: date.formatDate(
      sourceDate.valueOf(),
      `YYYY${splitterDate}MM${splitterDate}DD`
    ),
    time: date.formatDate(sourceDate.valueOf(), `HH${splitterTime}mm`),
  };
}

export function DateToUtc(sourceDate, time = '18:00') {
  const splittedDate = sourceDate.split('/');
  const splittedTime = time.split(':');

  const utcDate = date.buildDate(
    {
      year: +splittedDate[0],
      month: +splittedDate[1],
      date: +splittedDate[2],
      hours: +splittedTime[0],
      minute: +splittedTime[1],
    },
    false
  );

  const formatedDate = utcDate;
  return formatedDate;
}
