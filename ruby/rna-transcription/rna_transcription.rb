#### rna_transcription ####
#
#   Complement class with class method of_dna()
#       of_dna() takes in a DNA sequence as a string and returns
#       the complement RNA sequence. of_dna expects a string
#       and changes G, C, T, A to C, G, A, U respectively.
#
#   Complement.of_dna(<"DNA sequence">, allow_other = false, ignore_other = true)
#
#   Parameters:
#       <"DNA sequence"> : string
#           string of characters to be convertered
#
#       allow_other : bool (default: false)
#           boolean to allow other characters than DNA nucleotides to be processed.
#           if other character not allowed, of_dna returns '' for entire string if
#           any characters aren't DNA nucleotides (G, C, T, A).
#
#       ignore_other: bool (default: true)
#           boolean to to pass non-nucleotides back unchanged.
#           if false, all non-nucleotides are deleted from the sequence.
#
#   Returns:
#       <"RNA sequence"> : string
#           string with all the G, C, T, A changed to C, G, A, U


class Complement
  @@translation_table = {'G': 'C',
                         'C': 'G',
                         'T': 'A',
                         'A': 'U'}
    
  def self.of_dna(dna_sequence = "", allow_other = false, ignore_other = true) #-> ""
    if allow_other || dna_sequence.chars.all? {|nucleotide| @@translation_table.include? nucleotide.to_sym}
      return dna_sequence.chars.map {|nucleotide| translate(nucleotide, ignore_other)}.join
    else
      return ''
    end
  end

  def self.translate(nucleotide = '', ignore_other = true)
    if ignore_other || (@@translation_table.include? nucleotide.to_sym)
      return @@translation_table[nucleotide.to_sym]
    else
      return nucleotide
    end
  end

  private_class_method :translate

end

#### BookKeeping Version ####
#
#   the version of the tests that are being run
#

module BookKeeping
  VERSION = 4 # Where the version number matches the one in the test.
end
