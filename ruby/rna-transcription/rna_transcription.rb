#### rna_transcription ####
#
#   Complement class with class method of_dna()
#       of_dna() takes in a DNA sequence as a string and returns
#       the complement RNA sequence. of_dna expects a string and
#       changes G, C, T, A to C, G, A, U respectively. The string
#       must be sequences of G,C,T,A only, else an empty string
#       will be returned.
#
#   Complement.of_dna(<"DNA sequence">)
#
#   Parameters:
#       <"DNA sequence"> : string
#           string of characters to be convertered.
#           must be sequences of G,C,T,A only.
#
#   Returns:
#       <"RNA sequence"> : string
#           string with all the G, C, T, A changed to C, G, A, U;
#           or '' for non-compliant "DNA sequence".

class Complement
  @@DNA_to_RNA_table = {'G'=> 'C',
                        'C'=> 'G',
                        'T'=> 'A',
                        'A'=> 'U'}

  def self.of_dna(dna_sequence = "") #-> ""
    rna_sequence = ""
    dna_sequence.chars.each do |nucleotide|
      begin
        rna_sequence << @@DNA_to_RNA_table[nucleotide]
      rescue
        return ''
      end
    end
    rna_sequence
  end

end

#### BookKeeping Version ####
#
#   the version of the tests that are being run
#

module BookKeeping
  VERSION = 4 # Where the version number matches the one in the test.
end
