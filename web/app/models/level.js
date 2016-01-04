import DS from 'ember-data';

export default DS.Model.extend({
  level: DS.attr('number'),
  exp_at: DS.attr('number'),
  exp_of: DS.attr('number'),
  job: DS.belongsTo('job', { async: false }),
});
